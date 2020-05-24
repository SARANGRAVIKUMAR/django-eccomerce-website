from django.urls import path
from . import views

urlpatterns = [
    path("", views.view,name="view"),
    path("<slug>",views.update_cart,name = "update_cart"),
    path("<id>",views.remove_cart,name = "remove_cart"),


]