from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Feedback.as_view(), name ="feedback")
]