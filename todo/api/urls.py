from django.urls import path, include
from rest_framework import routers
from .views  import UserView, GroupView, CustomObtainPairView

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'groups', GroupView)



urlpatterns = [
  path('', include(router.urls)),
  path('login', CustomObtainPairView.as_view(), name='token_obtain_pair')
]
