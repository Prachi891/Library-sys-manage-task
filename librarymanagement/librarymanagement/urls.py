"""
URL configuration for librarymanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('add_book/',views.add_book,name='add_book'),
    path('borrow_record/',views.borrow_record,name='borrow_record'),
    path('book_list/',views.book_list,name='book_list'),
    path('export_authors/', views.export_authors_excel, name='export_authors'),
    path('export_books/', views.export_books_excel, name='export_books'),
    path('export_borrow_records/', views.export_borrow_records_excel, name='export_borrow_records'),
    path('show_books/', views.show_books, name='show_books'),
    path('export/',views.export,name='export'),

]