from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=5000, blank=True, null=True)
    thoughts = models.CharField(max_length=5000, blank=True, null=True)
    read_date = models.CharField(max_length=255, blank=True, null=True)
    add_date = models.DateTimeField('date added')
    def __str__(self):
        return self.title