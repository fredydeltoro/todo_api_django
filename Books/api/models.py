from django.db import models
from django.db.models import Sum
# Create your models here.


class AuthorQuerySet(models.QuerySet):
  use_for_related_fields = True

  def annotate_with_copies_sold(self):
    return self.filter(books__isnull=False).annotate(copies_sold=Sum('books__copies_sold'))


class Author(models.Model):
  # Make sure this manager is available.
  objects = AuthorQuerySet.as_manager()
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)

  def __str__(self):
    return self.first_name


class Book(models.Model):
  title = models.CharField(max_length=30)
  copies_sold = models.PositiveIntegerField()
  author = models.ForeignKey(
      Author, on_delete=models.CASCADE, related_name='books')

  def __str__(self):
    return self.title
