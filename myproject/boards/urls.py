from django.contrib import admin
from django.urls import include, path

from boards import views
from .views import home

urlpatterns = [
    # path(r'^$', home, name='home')
    path('home', views.home, name='home'),
]