from django.urls import path

from . import views

app_names = "hello"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("zdy", views.zdy, name="zdy"),
    path("David", views.david, name="david")
]