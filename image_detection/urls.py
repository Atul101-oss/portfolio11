from django.urls import path
from . import views

app_name = 'image_detection'

urlpatterns = [
    path('', views.detect_view, name='detect'),
    path('api/detect/', views.detect_api, name='detect_api'),
    path('history/', views.detection_history, name='history'),
]