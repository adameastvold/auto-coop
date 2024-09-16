from django.db import models

class Coop(models.Model):
   code = models.CharField(max_length=8, default="", unique=True)
   door = models.BooleanField(null=False, default=False)
   chicken_count = models.IntegerField(null=False, default=0)

