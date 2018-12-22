from . import views
from django.urls import path

urlpatterns = [
    path("", views.AboutUs.as_view(), name="aboutUs"),
]
