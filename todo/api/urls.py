from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from .views  import UserView, GroupView

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'groups', GroupView)



urlpatterns = [
  path('', include(router.urls)),
  path('login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair')
]
