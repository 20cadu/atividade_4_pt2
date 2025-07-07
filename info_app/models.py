from django.db import models
from django.db.models import ForeignKey, DateTimeField, TextField
from django.forms import CharField


# Create your models here.
class Person(models.Model):
    OPTIONS = [
        ("Female", "Female"),
        ("Male", "Male"),
        ("Others", "Others")
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=7, choices=OPTIONS, default='Male')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

class ContactLog(models.Model):
    person = ForeignKey(Person, on_delete=models.CASCADE)
    timestamp = DateTimeField(auto_now_add=True)
    message = TextField()