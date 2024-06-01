from django.urls import path
from . import views

urlpatterns = [
    path("", views.survey, name="poll"),
    path("result/", views.result, name="result")
]