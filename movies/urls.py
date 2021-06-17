from django.urls import path
from django.contrib import admin
from movies.views import index, show
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('show/' , show),
]