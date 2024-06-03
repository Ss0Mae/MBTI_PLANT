from django.urls import path
from . import views

app_name = 'poll'
urlpatterns = [
    path("", views.survey, name="survey"),
    path("result/", views.result, name="result")
]