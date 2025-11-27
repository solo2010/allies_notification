from django.urls import path
from . import views

app_name = 'mails'

urlpatterns = [
    path('', views.show, name='show'),
]
