from re import I
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from django.contrib.auth.models import update_last_login



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id' ,'username', 'password', 'last_login', 'refresh_token']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(str(password)) #hash password
        instance.save()
        return instance


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(TokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        # save refresh token into db
        serializer = UserSerializer(self.user, data= {"refresh_token": data["refresh"]}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # update last login
        update_last_login(None, self.user)

        return data


