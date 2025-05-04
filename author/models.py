from django.db import models

class Author(models.Model):
    name=models.CharField()
    bio=models.TextField()
    phone=models.CharField(max_length=13)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    enrolled_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
