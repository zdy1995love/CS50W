from django.urls import path

from . import views

app_names = "newyear"
urlpatterns = [
    path("", views.index, name="index")
]