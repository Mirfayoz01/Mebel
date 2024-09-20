from django.db import models
from django.views.generic import TemplateView


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=225)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    photo = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.title


class Karidor(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi



class Ofis(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Oshxona(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi

class Shkaf(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi

class Bolalar(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Kattalar(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi

class Tv(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi