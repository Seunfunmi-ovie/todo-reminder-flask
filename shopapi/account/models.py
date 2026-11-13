from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']


    def __str__(self):
        return self.email



class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    recipient_name = models.CharField(max_length=255, blank=True, null=True)
    line1 = models.CharField(max_length=255, blank=True, null=True)
    line2 = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length = 50)
    phone = models.CharField(max_length=11)
    is_default =models.BooleanField(default=False)


    def __str__(self):
        return(f"{self.user} {self.line1}")


