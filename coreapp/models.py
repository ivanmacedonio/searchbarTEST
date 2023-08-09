from django.db import models

class City(models.Model):
    country = models.CharField(max_length=128, null=False, blank=False)
    

class Guy(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    age = models.IntegerField()
    ciry = models.ForeignKey(City, on_delete=models.CASCADE)
