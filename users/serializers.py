from rest_framework import serializers
from authetifications.models import User
from rest_framework_simplejwt.views import token_obtain_pair
from users.models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(max_length=128, min_length=6, write_only=True)
  email = serializers.EmailField(required=True)
  username = serializers.CharField(required=True)
  class Meta:
    model = User
    fields = ('username', 'email', 'password',)

  def create(self, validated_data):
        # as long as the fields are the same, we can just use this
        # instance = self.Meta.model(**validated_data)
    instance = self.Meta.model(**validated_data)

    password = validated_data.pop('password', None)

    if password is not None:
      instance.set_password(password)
    instance.save()

    return instance


class LoginSerializer(serializers.ModelSerializer):
  password = serializers.CharField(max_length=128, min_length=6, write_only=True)
  class Meta:
    model = User
    fields = ('email', 'password')




class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']


    def create(self, validated_data):
        # as long as the fields are the same, we can just use this
        # instance = self.Meta.model(**validated_data)
      instance = self.Meta.model(**validated_data)

      password = validated_data.pop('password', None)

      if password is not None:
        instance.set_password(password)
      instance.save()

      return instance


"""
from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
"""

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


# Customizing token claims
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add more information about user
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = 'amosmoyo'
        token['email'] = user.email
        # token['is_superuser'] = user.is_superuser
        # token['is_staff'] = user.is_staff

        return token"""

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['id'] = self.user.id
        # data['groups'] = self.user.groups.values_list('name', flat=True)
        return data