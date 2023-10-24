from django.urls import path, include
from rest_framework import routers
from .views  import UserView, GroupView, CustomObtainPairView, TodoListView

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'groups', GroupView)

todo_list = TodoListView.as_view({
    'get': 'list',
    'post': 'create'
})



urlpatterns = [
  path('', include(router.urls)),
  path('login', CustomObtainPairView.as_view(), name='token_obtain_pair'),
  path('todos', todo_list, name='todos')
]
