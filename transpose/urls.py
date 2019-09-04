from django.urls import path

from . import views

app_name = 'transpose'
urlpatterns = [
    path('', views.index, name='index'),
    path('processing/', views.processing, name='processing'),
]