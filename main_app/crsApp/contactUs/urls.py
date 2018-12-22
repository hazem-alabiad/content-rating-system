from . import views
from django.urls import path

urlpatterns = [
    path("", views.ContactUs.as_view(), name="contactUs"),
]
