from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/addpage", views.addpage, name="addpage"),
    path("wiki/<str:title>", views.entry, name="entry")
]
