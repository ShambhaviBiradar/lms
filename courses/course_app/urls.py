from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test-video2', views.test_video, name='test_video'),
]
