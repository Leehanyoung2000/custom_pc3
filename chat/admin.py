from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import ChatRoom
# Register your models here.

admin.site.register(ChatRoom)