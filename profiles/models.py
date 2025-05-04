from django.db import models
from author.models import Author

class profiles(models.Model):
    name=models.CharField()
    about=models.TextField()
    author=models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
