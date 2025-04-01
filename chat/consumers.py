import json
import redis

from channels.generic.websocket import AsyncWebsocketConsumer


# Redis 클라이언트 생성
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """웹소켓 연결 시 실행"""
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # 채팅방 그룹에 추가
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # 클라이언트 연결 승인
        await self.accept()

        # 채팅방 인원 수 증가 및 가져오기
        user_count = await self.update_room_user_count(decrement=False)

        # 입장 메시지 전송
        welcome_message = f"{self.scope['user'].nickname} 님이 채팅방에 입장했습니다. (현재 인원: {user_count}명)"
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': welcome_message,
                'is_welcome': True,
                'username': self.scope['user'].username,
                'user_count': user_count  # 인원 수 추가
            }
        )

    async def disconnect(self, close_code):
        """웹소켓 연결 종료 시 실행"""
        # 채팅방 그룹에서 제거
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


        user_count = await self.update_room_user_count(decrement=True)

        # 퇴장 메시지 전송
        leave_message = f"{self.scope['user'].nickname} 님이 채팅방에서 퇴장했습니다.(현재 인원: {user_count}명)"
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': leave_message,
                'is_leave': True,
                'username': self.scope['user'].username,
                'user_count': user_count  # 인원 수 추가
            }
        )

    async def receive(self, text_data):
        """클라이언트로부터 메시지 수신 시 실행"""
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        # 메시지 로그 출력
        print(f"Received message: {message}, from username: {username}")

        # 방에 있는 모든 사용자에게 메시지 전송
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username
            }
        )

    async def chat_message(self, event):
        """채팅 메시지를 클라이언트로 전송"""
        message = event["message"]
        username = event["username"]

        # 메시지 로그 출력
        print(f"Sending message: {message} from username: {username}")

        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
            "is_welcome": event.get("is_welcome", False),
            "is_leave": event.get("is_leave", False),
            "user_count": event.get("user_count", None)  # 인원 수 추가
        }))

    async def update_room_user_count(self, decrement=False):
        """채팅방 인원 수 업데이트 (입장: +1, 퇴장: -1)"""
        user_count_key = f"room_user_count:{self.room_group_name}"

        # Redis에서 원자적으로 인원 수 업데이트
        if decrement:
            new_user_count = redis_client.decr(user_count_key)  # -1 감소
        else:
            new_user_count = redis_client.incr(user_count_key)  # +1 증가

        # 최소 인원 수를 0으로 유지 (음수 방지)
        if new_user_count < 0:
            redis_client.set(user_count_key, 0)
            new_user_count = 0

        return new_user_count  # 업데이트된 인원 수 반환

