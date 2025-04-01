from django.db import models
from django.contrib.auth import get_user_model  # 이 부분이 꼭 필요함!
User = get_user_model()
# Create your models here.



class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)  # 채팅방 이름
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간
    users = models.ManyToManyField(User, related_name="chat_rooms")  # 참여 유저

    def __str__(self):
        return self.name