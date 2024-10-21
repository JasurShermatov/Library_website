from django.urls import path
from .views import main_page, book_create, users_list
from .views import books_list
from .views import form_view


urlpatterns = [
    path('', main_page, name='main_page'),
    path("books/", books_list, name="books"),
    path('forma/', form_view, name='forma'),
    path('books/', books_list, name='book_details'),
    path('book_create/', book_create, name='book_create'),
    path('users/', users_list, name='users_list'),
]




