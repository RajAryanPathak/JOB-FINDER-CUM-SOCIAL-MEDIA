from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=400, null=True)
    phone = models.CharField(max_length=20, null=True)
    propic = models.ImageField(null=True, blank=True)
    Bio = models.CharField(max_length=800, null=True)

    def __str__(self):
        return self.user.username


class UserWebsite(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    li = models.CharField(max_length=200, null=True,default="")
    instagram = models.CharField(max_length=200, null=True,default="")
    github = models.CharField(max_length=200, null=True,default="")

    def __str__(self):
        return self.user.username


class UserEdu(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    TenName = models.CharField(max_length=200, null=True)
    tenthmarks = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    twelveName = models.CharField(max_length=200, null=True)
    Twelvwmarks = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    Graduationmarks = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    gradName = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username


class UserSkill(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    C = models.IntegerField(default=0,null=True)
    Cpp = models.IntegerField(default=0,null=True)
    python = models.IntegerField(default=0,null=True)
    java = models.IntegerField(default=0,null=True)
    webdev = models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    post = models.CharField(max_length=1000, null=True,default="")
    postpic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username+self.post
