from django.shortcuts import render
from rest_framework import response,status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import response
from rest_framework.decorators import api_view, permission_classes

from authetifications.models import User
from users.models import Profile
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, MyTokenObtainPairSerializer, UserSerializer

# Create your views here.
class Register(APIView):
    authentication_classes = []

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Custom user login
class LoginUser(APIView):
 def post(self, request, format='json'):
    User = get_user_model()
     
    email = request.data.get('email')
    password = request.data.get('password')

    res = Response()


    if (email is None) or (password is None):
      raise ValueError('username and password required')

    
    user = User.objects.filter(email=email).first()

    print('amosmoyo', user)

    if(user is None):
      raise ValueError('user not found')

    if (not user.check_password(password)):
        raise ValueError('wrong password')

    if user:
      serialized_user = LoginSerializer(user).data

      refresh = RefreshToken.for_user(user)

      access_token = str(refresh)
      refresh_token = str(refresh.access_token)

      res.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)

      res.data = {
          'success': 'true',
          'access_token': access_token,
          'refresh_token':refresh_token,
          'user': serialized_user,
      }

      return response.Response(res.data, status.HTTP_200_OK)
    
    return response.Response({'message': 'Invalid email or password'}, status.HTTP_401_UNAUTHORIZED)

# Customizing token claims
class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    # permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer


  # serializer_class = LoginSerializer

  # def post(self, request):
    # email = request.data.get('email', None)
    # password = request.data.get('password', None)

    # user = authenticate(username=email, password=password)

    # if user:
      # serializer = self.serializer_class(user)

      # return response.Response(serializer.data, status.HTTP_200_OK)
    
    # return response.Response({'message': 'Invalid email or password'}, status.HTTP_401_UNAUTHORIZED)
  

    """
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')

    user = User.objects.filter(username=username).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found')
    if (not user.check_password(password)):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_user = UserSerializer(user).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
    }

    return response
    """



"""
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
"""

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request, id):
  idData = int(id)
  userinfo = Profile.objects.get(user=idData)
  serializer = ProfileSerializer(userinfo, many=False)
  return Response(serializer.data)


@api_view(['GET'])
def getAllUser(request):
  user = Profile.objects.all()
  serializer = ProfileSerializer(user, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
  user = User.objects.all()
  serializer = ProfileSerializer(user, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def user(request):
  user = request.user
  serialized_user = UserSerializer(user).data

  return Response({'user': serialized_user })