from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Favourite(models.Model):
    person_id = models.ForeignKey(User, on_delete = models.CASCADE)
    Imdbid = models.CharField(max_length = 10,null=True)
    Title =models.CharField(max_length = 300,null=True)
    Year=models.CharField(max_length=5,null=True)
    Poster=models.CharField(max_length = 500,null=True)

    #def __str__(self):
    #    return self.Title
