from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class custom_user(AbstractUser):
    email=models.EmailField(unique=True)

class music_uploads_model(models.Model):
    date_time=models.DateTimeField(default=timezone.now)
    music_name=models.CharField(max_length=400)
    music_file=models.FileField(upload_to="music/")
    music_type=models.CharField(max_length=10)
    owner_email=models.ForeignKey(custom_user,to_field="email",on_delete=models.CASCADE,unique=False)
    def __str__(self):
        return f"{self.music_name} | {self.music_type} belong to {self.owner_email}"
class protected_accessors(models.Model):
    music_id=models.ForeignKey(music_uploads_model,to_field="id",on_delete=models.CASCADE,unique=False)
    email=models.ForeignKey(custom_user,to_field="email",on_delete=models.CASCADE,unique=False)
    def __str__(self):
        return f"{self.email}->{self.music_id}"
    class Meta:
        unique_together=("music_id","email")