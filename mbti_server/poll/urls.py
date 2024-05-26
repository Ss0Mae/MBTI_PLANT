from django.urls import path
from . import views

app_name = "poll"
urlpatterns = [
    path("", views.polls, name="polls"),
    path("result/", views.result, name="result")
]