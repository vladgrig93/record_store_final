from __future__ import unicode_literals
import bcrypt
from django.db import models

# Create your models here.
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors={}#no errors
        if len(postData['first_name'])<2 or len(postData['last_name'])<2:
            errors['name_error']='Name must be at least 2 characters long'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='Email is not valid'
        if len(postData['password'])<8 or len(postData['confirm_password'])<8:
            errors['pass_length']='Password must be 8 or more characters long'
        if postData['password']!=postData['confirm_password']:
            errors['passmatch']="Passwords don't match"
        if User.objects.filter(email=postData['email']):
            errors['exists']='Email is already taken'
        return errors
    def login_model(self, postData):
        errors={}
        user_to_check=User.objects.filter(email=postData['email'])#gets a full list
        if len(user_to_check)>0:
            user_to_check=user_to_check[0]#narrows it down to that user
            if bcrypt.checkpw(postData['password'].encode(), user_to_check.password.encode()):
                user={'user':user_to_check}
                return user
            else:
                errors={'error': "login Invalid"}
                return errors
        else:
            errors={'error': "login Invalid"}
            return errors
# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    admin=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class Record(models.Model):
    name=models.CharField(max_length=255)
    rec_image=models.TextField()
    price=models.IntegerField()
    genre=models.CharField(max_length=255)
    artist=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Cart(models.Model):
    owner=models.OneToOneField(User,related_name='shopping_cart')
    items=models.ManyToManyField(Record,related_name='carts')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Order(models.Model):
    status=models.BooleanField(default=False)
    user=models.ForeignKey(User, related_name='user_orders')
    recs=models.ManyToManyField(Record, related_name='orders')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Artist(models.Model):
    name=models.CharField(max_length=255)
    bio=models.TextField()
    art_image=models.TextField()
    record=models.ForeignKey(Record, related_name='artists')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    