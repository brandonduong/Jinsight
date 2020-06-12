from django.urls import path

from . import views

urlpatterns = [
    # ex: Homepage
    path('', views.index, name='index'),
    # ex: /create/
    path("create/", views.create, name="index"),

]