from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path("", views.index,name="index"),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("tracker/", views.tracker,name="tracker"),
    path("view/", views.view,name="view"),
    path("cart/", views.cart,name="cart"),
    path("search/", views.search,name="search"),
]