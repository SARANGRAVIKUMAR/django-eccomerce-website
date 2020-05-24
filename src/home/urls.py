from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/<slug>', views.single_product, name='single_product'),
    path('', views.search, name="search")
]
