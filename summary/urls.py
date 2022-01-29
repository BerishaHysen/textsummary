from django.urls import path
from summary import views


urlpatterns = [
    path('', views.index, name='index')
]