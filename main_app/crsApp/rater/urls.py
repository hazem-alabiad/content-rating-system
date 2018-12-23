from django.urls import path
from . import views

urlpatterns = [
    path("", views.Rater.as_view(), name ="rate")
]
