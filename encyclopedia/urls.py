from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/addpage", views.addpage, name="addpage"),
    path("wiki/save-page", views.save_page, name="save-page"),
    path("wiki/results", views.search_bar, name="search_page"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/save-edit", views.save_edit, name="save-edit")
]
