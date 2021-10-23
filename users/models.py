from django.db import models
from authetifications.models import User
from django.db.models.deletion import CASCADE
import uuid

# working with signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=200, blank=True, null=True)
  email = models.EmailField(max_length=500, blank=True, null=True)
  username = models.CharField(max_length=200, blank=True, null=True)
  location = models.CharField(max_length=200, blank=True, null=True)
  short_intro = models.CharField(max_length=200, blank=True, null=True)
  bio = models.TextField(blank=True, null=True)
  profile_img = models.ImageField(null=True, blank=True, upload_to="profiles", default="profiles/user-default.png")
  social_github = models.CharField(max_length=200, blank=True, null=True)
  social_twitter = models.CharField(max_length=200, blank=True, null=True)
  social_linkedin = models.CharField(max_length=200, blank=True, null=True)
  social_youtube = models.CharField(max_length=200, blank=True, null=True)
  social_website = models.CharField(max_length=200, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return str(self.username)
