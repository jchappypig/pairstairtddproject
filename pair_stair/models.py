from django.db import models

class Programmer(models.Model):
    name = models.TextField()

class Pair(models.Model):
    programmer1 = models.ForeignKey(Programmer, related_name="programmer1")
    programmer2 = models.ForeignKey(Programmer, related_name="programmer2")
    count = models.IntegerField()
