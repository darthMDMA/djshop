from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.views import LoginView
from .models import *
from .utils import django_slugify
from .utils import DataPostMixin
from django.contrib import messages
from .forms import *
from discussions.forms import DiscussionCreateForm, ReplyCreateForm
from discussions.models import Comment, Reply


side_bar = {'side_bar': {'Блог': 'blog',
                         'Все посты': 'all_posts_url',
                         'Мои посты': 'user_posts_url',
                         'Добавить пост': 'add_post_url',
                         'Тэги': 'all_tags_url',}}


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


class TagsList(ListView):
    model = Tag
    template_name = 'blog/all_tags.html'
    context_object_name = 'tag'

    def get_queryset(self):
        return Tag.objects.all().order_by('title')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {'title': 'тэги'}
        return dict(list(context.items()) + list(c_def.items()) + list(side_bar.items()))


class AddPost(CreateView):
    def get(self, request, *args, **kwargs):
        form = AddPostForm()
        request_dict = {'request': request}
        context = dict(list(side_bar.items()) + list(request_dict.items())+ list({'form': form,  'title': 'Добавить статью'}.items()))

        return render(request, 'blog/add_post.html', context=context)

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


class PostDetail(DetailView):
    def get(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['post_slug'], id=kwargs['post_id'])
        context = {
            'side_bar': side_bar['side_bar'],
            'title': post.title,
            'post': post,
            'form': DiscussionCreateForm(),
            'reply_form': ReplyCreateForm(),}
        return render(request, 'blog/post.html', context=context)

    def post(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['post_slug'], id=kwargs['post_id'])
        if 'comment_id' not in request.POST:
            b_f = DiscussionCreateForm(request.POST, instance=post)
            if b_f.is_valid():
                b_f.save(commit=False)
                b_f.save()
                comment = Comment(author=request.user,
                                  content=b_f.cleaned_data['content'],
                                  post=post)
                comment.save()
                post.comments.add(comment)
                messages.success(request, 'Комментарий добавлен')
                return HttpResponseRedirect(post.get_absolute_url())

        elif 'comment_id' in request.POST:

            c, a = request.POST['comment_id'].split('-')
            a = a.strip()
            comment = Comment.objects.get(pk=c)
            r_f = ReplyCreateForm(request.POST, instance=post)
            if r_f.is_valid():
                content = f"{a}, {r_f.cleaned_data['content']}" if a != str(request.user) else r_f.cleaned_data['content']
                reply = Reply(author=request.user,
                              content=content,
                              comment=comment)
                reply.save()
                comment.replies.add(reply)
                messages.success(request, 'Ответ на комментарий добавлен')
                return HttpResponseRedirect(post.get_absolute_url())

        context = {
            'side_bar': side_bar['side_bar'],
            'title': post.title,
            'post': post,
            'form': DiscussionCreateForm(),
        }
        return render(request, 'blog/post.html', context)


class EditPost(ModelFormMixin, DetailView):
    template_name = 'blog/edit_post.html'
    form_class = UpdatePostForm
    context_object_name = 'post'
    model = Post

    # def get_success_url(self):
    #     return reverse('post', kwargs={'post_id': self.object.pk, 'post_slug': self.object.slug, 'username': self.object.author})

    def get_object(self, queryset=None):
        post = Post.objects.get(id=self.kwargs['post_id'], slug__iexact=self.kwargs['post_slug'])
        return post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EditPost, self).get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.get_object())
        context['side_bar'] = side_bar['side_bar']
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()

        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        instance = form.save()
        instance.save()
        return super(EditPost, self).form_valid(form)


    #
    # def get(self, request, **kwargs):
    #
    #     form = UpdatePostForm
    #     template = 'blog/edit_post.html'
    #     post = Post.objects.get(id=kwargs['post_id'], slug__iexact=kwargs['post_slug'])
    #     context = {
    #         'form': form,
    #         'post': post,
    #         'side_bar': side_bar['side_bar']
    #     }
    #     return render(request, template, context)
    #
    # def post(self, request, username, post_slug, post_id):
    #     post = Post.objects.get(id=post_id, slug__iexact=post_slug)
    #     bound_form = UpdatePostForm(request.POST, request.FILES, instance=post)
    #
    #     if bound_form.is_valid():
    #         post.objects.updatte(title=bound_form.cleaned_data['title'])
    #         post.objects.updatte(content=bound_form.cleaned_data['content'])
    #         post.objects.updatte(tags=bound_form.cleaned_data['tags'])
    #         post.objects.updatte(photo=bound_form.cleaned_data['photo'])
    #         post.objects.updatte(id=post_id)
    #         post.objects.update(slug=post_slug)
    #         post.objects.update(author=username)
    #         post.save()
    #         return redirect(post)
    #     return render(request, 'blog/edit_post.html', {'form': bound_form})


def show_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    context = {
        'side_bar': side_bar['side_bar'],
        'title': tag.title,
        'post': tag.post_tags.all(),
        'tag': tag,
    }
    return render(request, 'blog/all_posts.html', context)


class DeletePost(DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('all_posts_url')
    template_name = 'blog/post.html'

    def get_object(self, queryset=None):
        post = Post.objects.get(id=self.kwargs['post_id'], slug__iexact=self.kwargs['post_slug'])
        return post

    def form_valid(self, form):
        messages.success(self.request, "Вы успешно удалили запись.")
        return super(DeletePost,self).form_valid(form)
