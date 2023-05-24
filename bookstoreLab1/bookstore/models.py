from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField("Book Name", max_length=255, unique=True)
    description = models.TextField("Book Description")
    author_name = models.CharField("Author Name", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    