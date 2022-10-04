from django.shortcuts import render

from .serializers import UserSerializer, LoginSerializer

from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework_simplejwt.views import TokenObtainPairView



class Register(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'data' : serializer.data,
                }, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Login(TokenObtainPairView):
    serializer_class = LoginSerializer


class Userview(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        data = UserSerializer(request.user).data
        return Response(data)


class DeleteUserview(APIView):
    permission_classes = [IsAuthenticated,]

    def delete(self, request):
        user=self.request.user
        user.delete()

        return Response({"result":"user delete"})