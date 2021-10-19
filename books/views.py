from books.models import Register, Books, BorrowBooks
from books.serializers import UserSerializer, LoginSerializer, AddBookSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserList(APIView):
    """
    List all Register, or create a new Register.
    """
    def get(self, request, format=None):
        register = Register.objects.all()
        serializer = UserSerializer(register, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login_User(APIView):
    '''Login User'''
    
    def post(self, request, format=None):

            serializer = LoginSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                data['response'] = 'User successfully Login'
                
            else:
                data['response'] = 'You have entered an invalid username or password'
            return Response(data)

class AddBookList(APIView):
    """
    List all Books, or create a new Books.
    """
    def get(self):
        register = Books.objects.all()
        serializer = AddBookSerializer(register, many=True)
        return Response(serializer.data)

        
    def post(self, request):

        serializer = AddBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
