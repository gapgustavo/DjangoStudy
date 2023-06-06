from django.db import models

# Create your models here.
class MoviesList(models.Model):
    name = models.TextField()
    resume = models.TextField()
    rank = models.DecimalField(decimal_places=2, max_digits=10)