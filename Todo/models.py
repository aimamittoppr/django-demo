from django.db import models


class Todo(models.Model):
    todo = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_target = models.DateField(blank=True)
