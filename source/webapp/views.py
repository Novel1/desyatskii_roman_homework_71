from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.db.models import Q

from django.views.generic import ListView, FormView

from accounts.forms import CommentForm
from posts.models import Post, Comment

# Create your views here.


class IndexView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['comment_form'] = CommentForm()
        return context


class PostDetailView(FormView):

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            author = request.user
            if not Comment.objects.filter(author=author, post=post).exists():
                Comment.objects.create(author=author, post=post, text=text)
        return redirect('index')


class CommentView(LoginRequiredMixin, FormView):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            author = request.user
            if not Comment.objects.filter(author=author, post=post).exists():
                Comment.objects.create(author=author, post=post, text=text)
        return redirect('index')


def search_users(request):
    queryset = request.GET.get('q')  # Get the search keyword from the GET parameters
    user_model = get_user_model()
    matching_users = user_model.objects.filter(
        Q(username__icontains=queryset) |
        Q(email__icontains=queryset) |
        Q(first_name__icontains=queryset)
    )
    users = []
    for user in matching_users:
        users.append({
            'name': user.get_full_name() or user.username,
            'url': reverse('profile', args=[user.pk])
        })
    return render(request, 'partial/search.html', {'users': users})
