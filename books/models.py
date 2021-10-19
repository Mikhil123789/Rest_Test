from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_count= models.IntegerField()
    
class BorrowBooks(models.Model):
    book_id = models.AutoField(primary_key=True)
    date= models.DateTimeField(auto_now_add=True)
