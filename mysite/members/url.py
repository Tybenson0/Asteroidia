from django.urls import path
from . import views

urlpatterns = [
    path('predictions', views.predictions, name='predictions'),
    path('model_testing', views.model_testing, name='model_testing'),
    path('raw_data', views.raw_data, name='raw_data'),
    path('main', views.main, name='main'),
    path('', views.main, name='main'),
]
