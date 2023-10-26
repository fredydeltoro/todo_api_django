from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import TodoList, Todo


class UserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  token = serializers.CharField(read_only=True)
  
  class Meta:
    model = User
    fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'token')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }
    
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError({"password": "Password fields didn't match."})
    
    return attrs
  
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    
    user.set_password(validated_data['password'])
    user.save()
    token = CustomTokenObtainPairSerializer.get_token(user)
    user.token = token
    
    return user
        

class ListSerializer(serializers.ModelSerializer):
  itemscount = serializers.IntegerField()
  
  class Meta:
    model = TodoList
    fields = ['id', 'name', 'description', 'user', 'itemscount']


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