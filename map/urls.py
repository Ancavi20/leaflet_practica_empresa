from django.urls import path

from . import views

app_name='map'

urlpatterns = [
    path('', views.mapa, name="mapa"),
    path('create_location/', views.create_location, name='create_location'),
    path('get_locations/', views.get_locations, name='get_locations'),
    path('edit_location/<int:location_id>/', views.edit_location, name='edit_location'),
    path('delete_location/<int:location_id>/', views.delete_location, name='delete_location'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
]