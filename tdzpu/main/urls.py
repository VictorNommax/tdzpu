from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.getcontent, name='home'),
    path('<int:pk>', views.ProductDetail.as_view(), name='product_detail'),

    path('about', views.getabout, name='about'),
    path('contacts', views.getcontacts, name='contacts'),
]
