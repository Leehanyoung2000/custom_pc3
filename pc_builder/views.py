from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from .models import User, Post, PCPartsBoard, Comment, Like
from .forms import PostForm, PcPartBoardForm, ProfileForm, CommentForm
from .functions import confirmation_required_redirect
from .mixins import LoginAndVerificationRequiredMixin, LoginAndOwnershipRequiredMixin

from braces.views import LoginRequiredMixin, UserPassesTestMixin

from allauth.account.models import EmailAddress
from allauth.account.views import PasswordChangeView

from urllib.parse import urlparse, parse_qs

import requests


# Create your views here.
class MouseListView(View):

    def get(self, request):
        page = request.GET.get("page")  # 현재 페이지 번호 가져오기
        API_URL = "http://127.0.0.1:8000/mouses"
        
        # 페이지가 있을 경우 URL에 page를 추가
        if page:
            API_URL = f"{API_URL}?page={page}"

        try:
            response = requests.get(API_URL)
            response.raise_for_status()  # 요청이 성공했는지 확인
            mouses_data = response.json()
            mouses = mouses_data.get("results", [])  # 마우스 목록 가져오기
            next_page = mouses_data.get("next")
            prev_page = mouses_data.get("previous")
            
            # next_page와 prev_page가 있다면 'page=' 뒤의 숫자를 추출
            if next_page:
                next_page = next_page.split('page=')[-1]  # page= 뒤의 번호 추출
            if prev_page:
                prev_page = prev_page.split('page=')[-1]  # page= 뒤의 번호 추출
                print("왜 안돼 진짜 짲으나네하;",prev_page)

        except requests.exceptions.RequestException as e:
            print(f"API 요청 중 오류 발생: {e}")
            mouses = []
            next_page = None
            prev_page = None

        return render(
            request,
            "pc_builder/mouse_list.html",
            {"mouses": mouses, "next_page": next_page, "prev_page": prev_page}
        )
class MouseDetailView(View):
    def get(self, request, pk):
        API_URL = f"http://127.0.0.1:8000/mouses/{pk}"
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            mouse = response.json()  # JSON 데이터 가져오기
            
        except requests.exceptions.RequestException as e:
            print(f"API 요청 중 오류 발생: {e}")
            mouse = None  # 오류 발생 시 None 처리
    
        return render(request, "pc_builder/mouse_detail.html",{"mouse":mouse})


class KeyboardListView(View):
    def get(self, request):
        page = request.GET.get("page")  # 현재 페이지 번호 가져오기
        API_URL = "http://127.0.0.1:8000/keyboard"
        
        # 페이지가 있을 경우 URL에 page를 추가
        if page:
            API_URL = f"{API_URL}?page={page}"

        try:
            response = requests.get(API_URL)
            response.raise_for_status()  # 요청이 성공했는지 확인
            keyboards_data = response.json()
            keyboards = keyboards_data.get("results", [])  # 마우스 목록 가져오기
            next_page = keyboards_data.get("next")
            prev_page = keyboards_data.get("previous")
            
            # next_page와 prev_page가 있다면 'page=' 뒤의 숫자를 추출
            if next_page:
                next_page = next_page.split('page=')[-1]  # page= 뒤의 번호 추출
            if prev_page:
                prev_page = prev_page.split('page=')[-1]  # page= 뒤의 번호 추출
                print("왜 안돼 진짜 짲으나네하;",prev_page)

        except requests.exceptions.RequestException as e:
            print(f"API 요청 중 오류 발생: {e}")
            keyboards = []
            next_page = None
            prev_page = None

        return render(
            request,
            "pc_builder/keyboard_list.html",
            {"keyboards": keyboards, "next_page": next_page, "prev_page": prev_page}
        )

class KeyboardDetailView(View):
    def get(self, request, pk):
        API_URL = f"http://127.0.0.1:8000/keyboard/{pk}"
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            keyboards = response.json()  # JSON 데이터 가져오기
            
        except requests.exceptions.RequestException as e:
            print(f"API 요청 중 오류 발생: {e}")
            keyboards = None  # 오류 발생 시 None 처리
    
        return render(request, "pc_builder/keyboard_detail.html",{"keyboards":keyboards})
        
class MonitorListView(View):
    def get(self, request):
        page = request.GET.get("page")  # 현재 페이지 번호 가져오기
        API_URL = "http://127.0.0.1:8000/monitor"
        
        # 페이지가 있을 경우 URL에 page를 추가
        if page:
            API_URL = f"{API_URL}?page={page}"

        try:
            response = requests.get(API_URL)
            response.raise_for_status()  # 요청이 성공했는지 확인
            monitors_data = response.json()
            monitors = monitors_data.get("results", [])  # 마우스 목록 가져오기
            next_page = monitors_data.get("next")
            prev_page = monitors_data.get("previous")
            
            # next_page와 prev_page가 있다면 'page=' 뒤의 숫자를 추출
            if next_page:
                next_page = next_page.split('page=')[-1]  # page= 뒤의 번호 추출
            if prev_page:
                prev_page = prev_page.split('page=')[-1]  # page= 뒤의 번호 추출
                print("왜 안돼 진짜 짲으나네하;",prev_page)

        except requests.exceptions.RequestException as e:
            print(f"API 요청 중 오류 발생: {e}")
            monitors = []
            next_page = None
            prev_page = None

        return render(
            request,
            "pc_builder/monitor_list.html",
            {"monitors": monitors, "next_page": next_page, "prev_page": prev_page}
        )

class MonitorDetailView(View):
    def get(self, request, pk):
        API_URL = f"http://127.0.0.1:8000/monitor/{pk}"
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            monitors = response.json()  # JSON 데이터 가져오기
            
        except requests.exceptions.RequestException as e:
            print(f"API 요청 중 오류 발생: {e}")
            monitors = None  # 오류 발생 시 None 처리
    
        return render(request, "pc_builder/monitor_detail.html",{"monitors":monitors})
        

class PcBuilderView(View):
    def get(self, request):
        API_BASE_URL = "http://127.0.0.1:8000"  # API 서버 주소

        try:
            # API에서 모니터, 마우스, 키보드 목록 가져오기
            monitors = requests.get(f"{API_BASE_URL}/monitor").json().get("results", [])
            mouses = requests.get(f"{API_BASE_URL}/mouses").json().get("results", [])
            keyboards = requests.get(f"{API_BASE_URL}/keyboard").json().get("results", [])

        except requests.exceptions.RequestException as e:
            print(f"API 요청 중 오류 발생: {e}")
            monitors, mouses, keyboards = [], [], []

        return render(
            request,
            "pc_builder/builder.html",
            {"monitors": monitors, "mouses": mouses, "keyboards": keyboards}
        )   

        
def index(request):
    print('인덱스 호출')
    return render(request, 'pc_builder/index.html')


class PostSearchView(ListView):
    model = Post
    context_object_name = 'search_results'
    template_name = 'pc_builder/search_results.html'
    paginate_by = 2
    def get_queryset(self):
        query = self.request.GET.get('query', '')

        return Post.objects.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get('query', '')
        return context
    

class ProfileView(DetailView):
    model = User
    template_name = 'pc_builder/profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name='profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile_user_id = self.kwargs.get('user_id')
        if user.is_authenticated:
            context['is_following'] = user.following.filter(id=profile_user_id).exists()
        context["user_posts"] = Post.objects.filter(author__id=profile_user_id).order_by('-dt_created')[:4]
        context["user_pcparts"] = PCPartsBoard.objects.filter(author__id=profile_user_id).order_by('-dt_created')[:4]
        
        return context

class ProfileSetView(LoginAndVerificationRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm 
    template_name = 'pc_builder/profile_set_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('index') 

class UserPostList(ListView):
    model = Post
    template_name = 'pc_builder/user_post_list.html'
    context_object_name = 'user_posts'
    paginate_by = 1

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Post.objects.filter(author__id=user_id).order_by('dt_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = get_object_or_404(User, id=self.kwargs.get("user_id"))
        return context

class UserPCPartList(ListView):
    model = PCPartsBoard
    template_name = 'pc_builder/user_pc_part_list.html'
    context_object_name = 'user_pc_parts'
    paginate_by = 1

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return PCPartsBoard.objects.filter(author__id=user_id).order_by('dt_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = get_object_or_404(User, id=self.kwargs.get("user_id"))
        return context


class PostList(ListView):
    model = Post
    template_name = 'pc_builder/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 2
    ordering = ["-dt_created"]

class PostListDetailView(DetailView):
    model = Post
    template_name = 'pc_builder/post_list_detail.html'
    context_object_name = 'post_detail'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['post_ctype_id'] = ContentType.objects.get(model='post').id
        context['comment_ctype_id'] = ContentType.objects.get(model='comment').id

        user = self.request.user
        if user.is_authenticated:
            post = self.object
            context['likes_post'] = Like.objects.filter(user=user, post=post).exists()
            context['likes_comment'] = Comment.objects.filter(post=post).filter(likes__user=user)


        return context


# 로그인 여부 판별 -> 이메일 인증 여부 판별 -> 작성
class PostCreateView(LoginAndVerificationRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    template_name = 'pc_builder/post_form.html'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post_form'] = context.get('form')  # 'form'을 'post_form'으로 할당
    #     return context

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'post_id': self.object.id})

class PostUpdateView(LoginAndOwnershipRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'pc_builder/post_form.html'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'post_id': self.object.id})   

class PostDeleteView(LoginAndOwnershipRequiredMixin, DeleteView):
    model = Post
    template_name = 'pc_builder/post_confirm_delete.html'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post_list')

class CommentCreateView(LoginAndVerificationRequiredMixin, CreateView):
    http_method_names = ['post']
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs.get('post_id'))

        return super().form_valid(form)


    def get_success_url(self):

        return reverse('post_detail', kwargs={'post_id':self.kwargs.get('post_id')})
    
class CommentUpdateView(LoginAndOwnershipRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'pc_builder/comment_update_form.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'post_id':self.object.post.id})


class CommentDeleteView(LoginAndOwnershipRequiredMixin, DeleteView):
    model = Comment
    template_name = 'pc_builder/comment_confirm_delete.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'post_id':self.object.post.id})

class PcPartList(ListView):
    model = PCPartsBoard
    template_name = 'pc_builder/pc_part_list.html'
    context_object_name = 'pc_part_list'
    paginate_by = 1
    ordering = ["-dt_created"]

class PcPartListDetailView(DetailView):
    model = PCPartsBoard
    template_name = 'pc_builder/pc_part_list_detail.html'
    context_object_name = 'pc_part_list_detail'
    pk_url_kwarg = 'pc_part_id'

class PcPartCreateView(LoginAndVerificationRequiredMixin, CreateView):
    model = PCPartsBoard
    form_class = PcPartBoardForm
    template_name = 'pc_builder/pc_part_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('pc_part_detail', kwargs={'pc_part_id': self.object.id})

class PcPartUpdateView(LoginAndOwnershipRequiredMixin,UpdateView):
    model = PCPartsBoard
    form_class = PcPartBoardForm
    
    template_name = 'pc_builder/pc_part_form.html'
    pk_url_kwarg = 'pc_part_id'

    def get_success_url(self):
        return reverse('pc_part_detail', kwargs={'pc_part_id': self.object.id})

class PcPartDeleteView(LoginAndOwnershipRequiredMixin, DeleteView):
    model = PCPartsBoard
    template_name = 'pc_builder/pc_part_confirm_delete.html'
    pk_url_kwarg = 'pc_part_id'
    context_object_name = 'pc_part'

    def get_success_url(self):
        return reverse('pc_part_list')

class ProcessLikeView(LoginAndVerificationRequiredMixin, View):
    http_method_names = ['post']
    def post(self, request, *args, **kwargs):
        # self.kwargs.get('content_type_id)
        # self.kwargs.get('object_id')

        # 유저가 댓글에 좋아요를 아직 누르지 않았다면 like 오브젝트 생성 
        # created는 true가 됩니다
        like, created = Like.objects.get_or_create(
            user = self.request.user,
            content_type_id = self.kwargs.get('content_type_id'),
            object_id = self.kwargs.get('object_id'),
        )

        # 이미 좋아요를 눌렀다면 like 오브젝트가 존재하기에 
        # created는 False가 됩니다.
        if not created:
            like.delete()
        
        return redirect(self.request.META['HTTP_REFERER'])

class ProcessFollowView(LoginAndVerificationRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile_user_id = self.kwargs.get('user_id')
        if user.following.filter(id=profile_user_id).exists():
            user.following.remove(profile_user_id)
        else:
            user.following.add(profile_user_id)
        
        return redirect('profile', user_id=profile_user_id)

class FollowingListView(ListView):
    model = User
    template_name = 'pc_builder/following_list.html'
    context_object_name = 'following'
    paginate_by = 3

    def get_queryset(self):
        profile_user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return profile_user.following.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user_id'] = self.kwargs.get('user_id')
        return context


class FollowerListView(ListView):
    model = User
    template_name = 'pc_builder/follower_list.html'
    context_object_name = 'followers'
    paginate_by = 3

    def get_queryset(self):
        profile_user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return profile_user.followers.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user_id'] = self.kwargs.get('user_id')
        return context

class CustomPasswordChangeView(PasswordChangeView):

    # 오버라이딩
    def get_success_url(self):
        return reverse('index')

    print('CustomPasswordChangeView 호출')
    