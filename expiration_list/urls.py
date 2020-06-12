from django.urls import path

from . import views

urlpatterns = [
    # ex: Homepage
    path('', views.index, name='index'),
    # ex: /create/
    path("create/", views.create, name="index"),
    # ex: /1/
    path("<int:id>", views.lists, name="lists"),
    # ex: /1/4/
    path("<int:id>/<int:itemId>/", views.delete, name="delete"),

]