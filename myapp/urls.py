
from django.urls import path
from myapp.views import RegisterView, LoginView, DashboardView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
     path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/dashboard/', DashboardView.as_view(), name='dashboard')
]