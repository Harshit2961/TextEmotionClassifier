from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('predict/', views.predict, name='predict')
]