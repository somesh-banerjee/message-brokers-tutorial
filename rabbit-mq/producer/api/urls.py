from django.urls import path
from . import views

urlpatterns = [
    path('send-message', views.AddMessageToQueue.as_view()),
]