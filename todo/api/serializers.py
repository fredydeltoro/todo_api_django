from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import TodoList, Todo


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']
        

class ListSerializer(serializers.ModelSerializer):
  class Meta:
    model = TodoList
    fields = ['id', 'name', 'description', 'user']


class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ['id', 'name', 'description', 'status', 'todo_list']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    # Add custom claims
    token['email'] = user.email
    token['username'] = user.username
    token['firstName'] = user.first_name
    token['lastName'] = user.last_name
    token['userId'] = user.id
    # ...
    
    return token
    
  def validate(self, attrs):
    data = super().validate(attrs)
    data['token'] = data['access']
    data.pop('access')
    
    return data