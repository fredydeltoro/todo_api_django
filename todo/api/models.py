from django.db import models
from django.contrib.auth import get_user_model
from model_utils.fields import AutoCreatedField, AutoLastModifiedField

User = get_user_model()

# Create your models here.
class TodoList(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False)
  description = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = AutoCreatedField()
  updated_at = AutoLastModifiedField()
  
  def __str__(self):
    return self.name
      

class Todo(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False)
  description = models.TextField()
  status = models.BooleanField(default=False)
  todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
  created_at = AutoCreatedField()
  updated_at = AutoLastModifiedField()
  
  def __str__(self):
    return self.name
