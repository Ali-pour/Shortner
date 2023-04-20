from django.db import models
from django.contrib.auth.models import User


class Full_link(models.Model):
    full_link = models.CharField(max_length=300)

    def __str__(self):
        return self.full_link


class Short_link(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    full_id = models.ForeignKey(Full_link, on_delete=models.CASCADE)
    short_link = models.CharField(max_length=6)

    def __str__(self):
        return self.short_link