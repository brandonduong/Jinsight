from django.urls import path

from . import views

urlpatterns = [
    # ex: /register/
    path('register/', views.register, name='register')
]