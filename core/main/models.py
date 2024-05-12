from django.db import models

# Create your models here.

class TodoList(models.Model):

    name = models.CharField('Todo name', max_length = 100)