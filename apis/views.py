from django.db import models
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.response import Response
from projects.models import Projects
from .serializer import Projectserializer
from rest_framework.permissions import IsAuthenticated



