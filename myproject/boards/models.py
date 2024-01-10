from django.db import models
from django.urls import reverse

class קטגוריה(models.Model):
    שם = models.CharField(max_length=100)
    def __str__(self):
        return self.שם

class מוצר(models.Model):
    שם = models.CharField(max_length=100)
    קטגוריה = models.ForeignKey(קטגוריה, on_delete=models.CASCADE)
    def __str__(self):
        return self.שם

class ספק(models.Model):
    שם = models.CharField(max_length=100)
    def __str__(self):
        return self.שם

class הזמנה(models.Model):
    מוצר = models.ForeignKey(מוצר, on_delete=models.CASCADE)
    ספק = models.ForeignKey(ספק, on_delete=models.CASCADE)
    כמות = models.IntegerField()
    תאריך = models.DateField()