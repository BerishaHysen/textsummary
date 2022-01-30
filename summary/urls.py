from django.urls import path
from summary import views


urlpatterns = [
    path('', views.index, name='index'),
    path('summary_page', views.summary_page, name='summary_page'),
    path('save_summary', views.save_summary, name='save_summary'),
    path('history', views.history, name='history'),
    path('history_topic', views.history_topic, name='history_topic')
]