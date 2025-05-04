from django.db import models
from category.models import category
from author.models import Author

class post(models.Model):
    title=models.CharField()
    content=models.TextField()
    category=models.ManyToManyField(category)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
