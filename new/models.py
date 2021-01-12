from django.db import models


class Todo(models.Model):
    cat = models.CharField(max_length=20)
    def __str__(self):
        return self.cat


class Jag(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=50)
    dob = models.DateField()
    end_time = models.DateField()
    ph = models.ImageField(upload_to ='static/',blank = True)
    cat = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
