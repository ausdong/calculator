from django.db import models

# Create your models here.
class CalcString(models.Model):
    def __str__(self):
        return self.ctext
    ctext = models.CharField(max_length=200)
    num = models.CharField(max_length=100)
    first = models.FloatField()
    second = models.FloatField()
    op = models.CharField(max_length=2)

class StoredNum(models.Model):
    def __str__(self):
        return self.stored
    stored = models.FloatField()

class Result(models.Model):
    def __str__(self):
        return self.ans
    ans = models.FloatField()

class Previous(models.Model):
    def __str__(self):
        return self.val
    val = models.FloatField()
    pop = models.CharField(max_length=2)
