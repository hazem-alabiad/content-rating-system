from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Rater.as_view(), name ="rate"),
    path("feedback", include("feedback.urls"))
]
