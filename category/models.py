from django.db import models

class category(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name