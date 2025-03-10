from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=255)
    long = models.DecimalField(max_digits=23, decimal_places=20)
    lat = models.DecimalField(max_digits=23, decimal_places=20)

    def __str__(self):
        return self.name


class PasswordType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Password(models.Model):
    value = models.CharField(max_length=255)
    password_type = models.ForeignKey(PasswordType, on_delete=models.RESTRICT)
    place = models.ForeignKey(Place, on_delete=models.RESTRICT)

    def __str__(self):
        return self.value


class Comment(models.Model):
    text = models.TextField()
    password = models.ForeignKey(Password, on_delete=models.RESTRICT)

    # commenting this out for now - the textfield is giving some sort of
    # error, and I'm not sure we need this anyway.
    # def __str__(self):
    #    self.text
