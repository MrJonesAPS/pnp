from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=255)
    long = models.DecimalField(max_digits=23, decimal_places=20)
    lat = models.DecimalField(max_digits=23, decimal_places=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CodeType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Code(models.Model):
    value = models.CharField(max_length=255)
    code_type = models.ForeignKey(CodeType, on_delete=models.RESTRICT)
    place = models.ForeignKey(Place, on_delete=models.RESTRICT)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Vote')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value

class Vote(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    worked = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    text = models.TextField()
    code = models.ForeignKey(Code, on_delete=models.RESTRICT)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # commenting this out for now - the textfield is giving some sort of
    # error, and I'm not sure we need this anyway.
    # def __str__(self):
    #    self.text
