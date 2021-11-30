from django.urls import path
from . import views


urlpatterns = [
    path('', views.gethead, name="gethead"),
]
