from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation




from .validators import validate_no_special_characters

# Create your models here.
class User(AbstractUser):

    nickname = models.CharField(
        max_length=15, unique=True, null=True,
        validators =[validate_no_special_characters],
        error_messages={"unique":"이미 사용중인 닉네임입니다."},
        
        )

    profile_pic = models.ImageField(default="default_profile_pic.jpg", upload_to='profile_pics')

    intro = models.CharField(max_length=60, blank=True)

    following = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        blank=True,
        related_name='followers')



class Post(models.Model):
    title = models.CharField(max_length=30)

    image1 = models.ImageField(upload_to='post_pics', blank=True)

    image2 =  models.ImageField(upload_to='post_pics', blank=True)

    image3 = models.ImageField(upload_to='post_pics', blank=True)

    content = models.TextField()

    dt_created = models.DateTimeField(auto_now_add=True)
    
    dt_updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
    likes = GenericRelation('Like', related_query_name='post')
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-dt_created']



class PCPartsBoard(models.Model):
    CATEGORY_CHOICES = [
        ('cpu', 'cpu'),
        ('keyboard', 'keyboard'),
        ('mouse', 'mouse'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    image1 = models.ImageField(upload_to='part_pics', blank=True)

    image2 = models.ImageField(upload_to='part_pics', blank=True)

    image3 = models.ImageField(upload_to='part_pics', blank=True)


    title = models.CharField(max_length=30)

    content = models.TextField()

    dt_created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-dt_created']    


class Comment(models.Model):
    content = models.TextField(max_length=500, blank=False)

    dt_created = models.DateTimeField(auto_now=True)

    dt_updated = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    likes = GenericRelation('Like',related_query_name='comment')

    def __str__(self):
        return self.content[:30]
    

class Like(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    liked_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return F"({self.user}, {self.liked_object})"
    