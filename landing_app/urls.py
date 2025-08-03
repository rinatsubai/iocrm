from django.urls import path
from landing_app import views

urlpatterns = [
    path("", views.home, name="home"),
]
