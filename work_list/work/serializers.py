from rest_framework import serializers
from .models import Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['work_id', 'title', 'content', 'status', 'start_date', 'end_date', 'user']
