from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('jasur/', admin.site.urls),
    path('', include('library.urls')),
]

