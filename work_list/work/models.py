from django.db import models
from user.models import User

# Create your models here.
class Work(models.Model):
    work_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User ,on_delete=models.CASCADE, default = '')