from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User 
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .permissions import HasRole
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'message': 'User logged in successfully'})
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class DashboardView(APIView):
    permission_classes = [IsAuthenticated,HasRole]
    required_role = 'Software engg.'
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({
            'message': "Welcome to the dashboard",
            'user': serializer.data,
        }, status=status.HTTP_200_OK)
    
