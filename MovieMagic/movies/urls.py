from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:movie_id>', views.details, name='detail'),
    path('add', views.add, name='add'),
    path('edit/<int:movie_id>', views.edit, name='edit'),
    path('delete/<int:movie_id>',views.delete, name='delete'),

]
