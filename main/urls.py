from django.contrib import admin
from django.urls import path, include
from .views import index, add_book_page, detail_book_page, delete_book, update_book_page, similarity_checker


app_name = "main"
urlpatterns = [
    path('', index, name='home'),
    path('add-book/', add_book_page, name='add-book'),
    path('detail-book/<int:id>', detail_book_page, name='detail-book'),
    path('delete-book/<int:id>', delete_book, name='delete-book'),
    path('update-book/<int:id>', update_book_page, name='update-book'),
    path('similarity-checker/', similarity_checker, name='similarity-checker')
]
