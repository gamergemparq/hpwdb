# pyright: reportMissingModuleSource=false
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.index, name="index"),
    path('home', views.home, name="home"),
    path('create/', views.create, name="create")
]
