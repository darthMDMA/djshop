from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .utils import django_slugify
from .utils import DataPostMixin
from django.contrib import messages
from .forms import *


side_bar = {'side_bar': {'Блог': 'blog', 'Все посты': 'all_posts', 'Мои посты': 'user_posts', 'Добавить пост': 'add_post'}}


def blog_home(request):
    request_dict = {'request': request}
    context = dict(list(side_bar.items()) + list(request_dict.items()))
    return render(request, template_name='blog/index.html',context=context)


class PostsListView(DataPostMixin, ListView):

    def get_queryset(self):
        return Post.objects.all().order_by('-date_created')

    def get_context_data(self, *, object_list=None, **kwargs):  # данная функция используется для динамисеских обьектов
        context = super().get_context_data(**kwargs)  # обращаемся к базовому классу View и берем существующий контекст -> dict
        c_def = {'title': 'Статьи'}
        return dict(list(context.items()) + list(c_def.items()) + list(side_bar.items()))


class UserPostListView(DataPostMixin, ListView):

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')

    def get_context_data(self, *, object_list=None, **kwargs):  # данная функция используется для динамисеских обьектов
        context = super().get_context_data(**kwargs)  # обращаемся к базовому классу View и берем существующий контекст -> dict
        c_def = {'title': 'Статьи пользователя'}
        return dict(list(context.items()) + list(c_def.items()) + list(side_bar.items()))


class AddPost(ListView):

    def get(self, request, *args, **kwargs):
        form = AddPostForm()
        request_dict = {'request': request}
        context = dict(list(side_bar.items()) + list(request_dict.items())+ list({'form': form,  'title': 'Добавить статью'}.items()))

        return render(request, 'blog/add_post.html', context=context)


    def Test(selfdunction):
        pass


    def post(self, request, *args, **kwargs):
        new_post = Post(author=request.user, slug=django_slugify(request.POST['title']))
        bound_form = AddPostForm(request.POST, request.FILES, instance=new_post)
        if bound_form.is_valid():
    # еще вариант изменения данных
    # post = form.save(commit=False)
    # post.title = request.user
    # post.slug = request.POST['title']
            bound_form.save()
            messages.success(request, 'статья успешно добавлена!!!')
            return redirect(new_post)
        return render(request, 'blog/add_post.html', {'form': bound_form})


def show_post(request, **kwargs):

    post = get_object_or_404(Post, slug=kwargs['post_slug'], id=kwargs['post_id'])
    context = {
        'side_bar': side_bar['side_bar'],
        'title': post.title,
        'post': post
    }

    return render(request, 'blog/post.html', context=context)