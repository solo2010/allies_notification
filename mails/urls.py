from django.urls import path
from . import views

app_name = 'mails'

urlpatterns = [
    path('', views.show, name='show'),
    path('create', views.create, name='create'),
    path('get_templates', views.get_templates, name='get_templates'),
]
