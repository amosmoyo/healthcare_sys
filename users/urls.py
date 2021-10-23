from django.urls import path

from .views import Register, LoginUser, getProfile, getAllUser, CustomTokenObtainPairView, getUsers, user

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users import views

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('profile/<str:id>', views.getProfile, name='user_profile' ),
    path('getusers/', views.getAllUser, name="users"),
]
