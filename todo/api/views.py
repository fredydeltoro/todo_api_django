from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from .models import TodoList
from .serializers import UserSerializer, GroupSerializer, ListSerializer

class UserView(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class GroupView(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  
class CustomObtainPairView(TokenObtainPairView):
  def post(self, request, *args, **kwargs):
    username = request.data['user']
    
    if username.find('@') > 0:
      try:
        user = User.objects.get(email=username)
        username = user.username
      except:
        pass
    
    request.data['username'] = username
    
    return super().post(request, *args, **kwargs)
  

class TodoListView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ListSerializer
    
    def get_queryset(self):
      return TodoList.objects.all().filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
      request.data['user'] = request.user.id
      return super().create(request, *args, **kwargs)