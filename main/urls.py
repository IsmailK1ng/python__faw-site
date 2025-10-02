from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('become-a-dealer/', views.products, name='become_a_dealer'),
    path('lizing/', views.products, name='lizing'),
    path('news/', views.products, name='news'),
    path('products/', views.products, name='products'),
    path('dealers/', views.products, name='dealers'),
    path('jobs/', views.products, name='jobs'),
]