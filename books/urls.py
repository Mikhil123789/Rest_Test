from django import urls
from django.urls import path, include
from . import views
from .views import  UserList, Login_User, AddBookList

urlpatterns = [

    path('register_user/', views.UserList.as_view()),
    path('login_user/', views.Login_User.as_view()),
    path('add_book/', views.AddBookList.as_view()),

    
]
