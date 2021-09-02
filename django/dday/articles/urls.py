from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('getdate/', views.getdate, name='getdate'),
    path('result/', views.result, name='result'),
]