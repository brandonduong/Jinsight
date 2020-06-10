from django.urls import path

from . import views

urlpatterns = [
    # ex: Homepage
    path('', views.index, name='index'),
]