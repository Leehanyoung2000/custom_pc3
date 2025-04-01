from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),

    # Post
    path("posts/", views.PostList.as_view(), name="post_list"),
    path("posts/<int:post_id>/", views.PostListDetailView.as_view(), name="post_detail"),
    path('posts/new/', views.PostCreateView.as_view(), name='post_form'),
    path('posts/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    path('search/', views.PostSearchView.as_view(), name='search'),

    # PCPartsBoard
    path('pc_parts/', views.PcPartList.as_view(), name='pc_part_list'),
    path('pc_parts/<int:pc_part_id>/', views.PcPartListDetailView.as_view(), name='pc_part_detail'),
    path('pc_parts/new/',views.PcPartCreateView.as_view(), name='pc_part_form'),
    path('pc_parts/<int:pc_part_id>/edit/', views.PcPartUpdateView.as_view(), name='pc_part_edit'),
    path('pc_parts/<int:pc_part_id>/delete/', views.PcPartDeleteView.as_view(), name='pc_part_delete'),
    
    # Profile
    path('users/<int:user_id>/', views.ProfileView.as_view(), name='profile'),
    path('users/<int:user_id>/posts/', views.UserPostList.as_view(), name='user_post_list'),
    path('users/<int:user_id>/pc_parts/', views.UserPCPartList.as_view(), name='user_pc_part_list'),
    path('set_profile', views.ProfileSetView.as_view(), name='profile_set'),

    # Comment
    path(
        'posts/<int:post_id>/comments/create',
        views.CommentCreateView.as_view(),
        name='comment_create',
    ),
    path('comments/<int:comment_id>/edit/', views.CommentUpdateView.as_view(),name='comment_update'),
    path('comments/<int:comment_id>/delete/', views.CommentDeleteView.as_view(),name='comment_delete'),


    # Like
    path('like/<int:content_type_id>/<int:object_id>/', views.ProcessLikeView.as_view(), name='process_like'),


    # following
    path(
        'users/<int:user_id>/follow/',
        views.ProcessFollowView.as_view(),
        name='process_follow'
    ),
    path(
        'users/<int:user_id>/following/', 
        views.FollowingListView.as_view(), 
        name='following_list'
    ),
    path(
        'users/<int:user_id>/followers/', 
        views.FollowerListView.as_view(), 
        name='follower_list'
    ),


    # api 
    path("mouses/", views.MouseListView.as_view(), name="mouse_list"),
    path("mouses/<int:pk>", views.MouseDetailView.as_view(), name="mouse_detail"),

    path('keyboard/', views.KeyboardListView.as_view(), name='keyboard_list'),
    path('keyboard/<int:pk>', views.KeyboardDetailView.as_view(), name='keyboard_detail'),

    path('monitor/', views.MonitorListView.as_view(), name='monitor_list'),
    path('monitor/<int:pk>', views.MonitorDetailView.as_view(), name='monitor_detail'),

    path('builder/', views.PcBuilderView.as_view(), name='builder'),
]
