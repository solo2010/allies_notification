from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.show, name='show'),
    path('<int:group_id>/partners', views.show, name='show_for_group'),
    path('create', views.create, name='create'),
    path('create/<int:group_id>', views.create, name='create_for_group'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete/<int:id>/<int:group_id>', views.delete, name='delete_for_group'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/<int:id>/<int:group_id>', views.edit, name='edit_for_group'),
]

