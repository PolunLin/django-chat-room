# chat/urls.py
from django.urls import path
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = "chat"


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),

]


if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )