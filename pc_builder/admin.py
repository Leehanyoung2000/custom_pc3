from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import User, Post, PCPartsBoard, Like, Comment
# Register your models here.
admin.site.register(User, UserAdmin)


class CommentInline(admin.StackedInline):
    model = Comment

class LikeInline(GenericStackedInline):
    model = Like

class UserInline(admin.StackedInline):
    model = User.following.through
    fk_name = 'to_user'
    verbose_name = 'Follower'
    verbose_name_plural = 'Followers'

UserAdmin.fieldsets += ('Custom fields', {'fields': ('nickname','intro','profile_pic','following')}),
UserAdmin.inlines = (UserInline,)
class PostAdmin(admin.ModelAdmin):
    inlines =(
        CommentInline,
        LikeInline,
    )

class CommentAdmin(admin.ModelAdmin):
    inlines =(
        LikeInline,
    )

admin.site.register(Post, PostAdmin)
admin.site.register(PCPartsBoard)
admin.site.register(Like)
admin.site.register(Comment, CommentAdmin)
