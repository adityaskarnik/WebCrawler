from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('url_submitted', views.submit, name='submit')
]