from django.urls import path
from . import views

app_name = 'DIP'
urlpatterns = [
    path('', views.home, name='dip_home'),
    path('work/<slug:title>', views.image_transformation, name='image_transformation'),
    
]
