from django.urls import path
from . import views


urlpatterns = [
    path('', views.toComments, name='feedback'),
]
