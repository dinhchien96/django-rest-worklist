from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Work(models.Model):
    work_id = models.AutoField(primary_key=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)