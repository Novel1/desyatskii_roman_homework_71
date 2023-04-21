from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.forms import LoginForm, CustomUserCreationForm, UserChangeForm, PostForm

from posts.models import Post, Like


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, 'Пользователь не найден')
            return redirect('login')
        messages.success(request, 'Добро пожаловать!')
        login(request, user)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


class RegistrationView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class ProfileView(DetailView, PermissionRequiredMixin):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    permission_required = 'accounts.user_change'
    permission_denied_message = 'У вас не хватает прав доступа'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all()
        return context


class UserChangeView(UpdateView, PermissionRequiredMixin):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_queryset(self):
        return Post.objects.prefetch_related('comments')

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            form.save()
            return redirect('/')
        contex = {'form': form}
        return self.render_to_response(contex)


# views.py
def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        author = request.user
        like, created = Like.objects.get_or_create(author=author, post=post)
        if not created:
            like.delete()
        post.likes_count = post.post_like.count()
        post.save()
        return redirect('index')
    return redirect('index')






