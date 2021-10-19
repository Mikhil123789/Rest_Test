from django.db.models import fields
from rest_framework import serializers
from .models import Register, Books

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id','name','email','password']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['email', 'password']
class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['book_name', 'author','book_count']
