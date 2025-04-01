# chat/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatRoom



def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def chat_room_list(request):
    # 모든 채팅방을 가져와서 템플릿에 전달
    chat_rooms = ChatRoom.objects.all()  # 또는 필요한 필터 추가
    return render(request, "chat/chat_room_list.html", {"chat_rooms": chat_rooms})


@csrf_exempt  # CSRF 보호를 비활성화 (POST 요청에 CSRF 검사 비활성화)
def chat_room_create(request):
    if request.method == "POST":
        # 폼에서 받은 데이터로 채팅방 생성
        room_name = request.POST.get("name")
        if room_name:
            new_room = ChatRoom.objects.create(name=room_name)
            return redirect('chat_room_list')  # 생성 후 방 목록으로 리디렉션
    return render(request, "chat/chat_room_create.html")