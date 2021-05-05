from django.db import models

# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    #phone = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    repeat_password = models.CharField(max_length=10)

    def __str__(self):
        return self.username
'''
class User(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()

    class Meta:
        db_table='suscribed_user'

    def __str__(self):
        return self.username  
'''