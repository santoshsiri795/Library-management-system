from django.db import models

# Create your models here.

class Library(models.Model):
    Book_name = models.CharField(max_length=1000)
    Author_name = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.Book_name
