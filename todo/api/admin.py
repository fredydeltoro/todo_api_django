from django.contrib import admin
from .models import TodoList, Todo


class ListAdmin(admin.ModelAdmin):
  list_display = ('name', 'user')


# Register your models here.
admin.site.register(TodoList, ListAdmin)
admin.site.register(Todo)
