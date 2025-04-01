# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("rooms/", views.chat_room_list, name="chat_room_list"),  
    path("create/", views.chat_room_create, name="chat_room_create"),  
    path("<str:room_name>/", views.room, name="room"),
]
