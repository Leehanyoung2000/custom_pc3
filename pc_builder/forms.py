from django import forms

from .models import User, Post, PCPartsBoard, Comment





# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'nickname',
#         ]
#     def signup(self, request, user):
#         user.nickname = self.cleaned_data["nickname"]
#         user.save()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'image1', 
            'image2', 
            'image3',
            'content', 
        ]


class PcPartBoardForm(forms.ModelForm):
    class Meta:
        model = PCPartsBoard
        fields = [
            'category',
            'image1',  
            'image2',
            'image3', 
            'title', 
            'content', 
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'nickname',
            'profile_pic',
            'intro',
        ]

        widgets={
            "intro": forms.Textarea,
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        widgets = {
            'content' : forms.Textarea,
        }