"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work.views import Emp,book,booklist,pdetail,book_one,student,studename,book_del

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',Emp.as_view()),
    path('do/',book.as_view()),
    path('book/',booklist.as_view(),name="book-det"),
    path("book/<int:pk>",book_one.as_view(),name="book-detail"),
    path('book/<int:pk>/re',book_del.as_view(),name="book-del"),
    path('stud/',student.as_view()),
    path('studna/<int:pk>',studename.as_view()),
     path('pdetails/',pdetail.as_view()),
   
]
