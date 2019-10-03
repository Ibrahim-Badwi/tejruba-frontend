from rest_framework import generics

from .models import CustomUser
from .serializers import CustomUserSerializer


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer