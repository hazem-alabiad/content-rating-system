from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Search.as_view(), name ="search"),
    path("query", views.Search.as_view(), name ="query")
]