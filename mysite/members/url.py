from django.urls import path
from . import views

urlpatterns = [
    path('predictions', views.predictions, name='predictions'),
    path('model_testing', views.model_testing, name='model_testing'),
]
