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

todo_list_detail = TodoListView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
  path('', include(router.urls)),
  path('login', CustomObtainPairView.as_view(), name='token_obtain_pair'),
  path('todos', todo_list, name='todos'),
  path('todos/<int:pk>', todo_list_detail, name='todo_list_detail')
]
