from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

class UserView(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class GroupView(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer