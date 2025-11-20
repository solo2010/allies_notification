from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.show, name='show'),
    path('<int:group_id>/partners', views.show, name='show_for_group'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
]

