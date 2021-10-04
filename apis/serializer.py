from django.db import models
from django.db.models import fields
from rest_framework import serializers



class ProfileSerializer(serializers.ModelSerializer):
    fields = '__all__'

