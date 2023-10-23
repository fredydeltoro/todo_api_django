from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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