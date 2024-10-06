from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.DecimalField(max_digits=4, decimal_places=3)
    description = models.CharField(max_length=100)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title


