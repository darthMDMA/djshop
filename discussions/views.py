from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


side_bar = {'side_bar': {'Блог': 'blog', 'Все посты': 'all_posts','Мои посты': 'user_posts', 'Добавить пост': 'add_post'}}


def discussions_home(request):
    request_dict = {'request': request}
    context = dict(list(side_bar.items()) + list(request_dict.items()))
    return render(request, template_name='discussions/discussions_index.html',context=context)


#
@login_required
def discussion_create(request):

    if request.method == "POST":

        form = DiscussionCreateForm(request.POST, request.FILES)

        if form.is_valid():
            new_discussion = form.save(commit=False)
            new_discussion.author = request.user
            new_discussion.save()

        else:

            form = DiscussionCreateForm()
#
#
        return render(request, "discussions/create_form.html", context=Discussion)