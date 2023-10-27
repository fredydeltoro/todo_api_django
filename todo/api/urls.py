from django.urls import path
from .views import UserView, CustomObtainPairView, TodoListView, TodoView


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

todo_item_list = TodoView.as_view({
    'get': 'list',
    'post': 'create'
})

todo_detail = TodoView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('signup', UserView.as_view(), name='register'),
    path('login', CustomObtainPairView.as_view(), name='token_obtain_pair'),
    path('todos', todo_list, name='todos'),
    path('todos/<int:pk>', todo_list_detail, name='todo_list_detail'),
    path('todos/<int:list_id>/items', todo_item_list, name='todo_items'),
    path('todos/<int:list_id>/items/<int:pk>', todo_detail, name='todo_detail')
]
