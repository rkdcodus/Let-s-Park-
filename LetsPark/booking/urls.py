from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("park/", views.park, name="park"),
    path("park/<int:pk>", views.booking, name="booking"),
    path("mybooking/", views.mybooking, name="mybooking")

]
