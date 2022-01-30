from django.urls import path
from summary import views


urlpatterns = [
    path('', views.index, name='index'),
    path('summary_page', views.summary_page, name='summary_page')
]