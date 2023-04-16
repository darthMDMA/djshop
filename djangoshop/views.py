import os
from .settings import BASE_DIR
from django.shortcuts import render
from blog import views

app_name_path = os.path.join(BASE_DIR, '')


def home_view(request):
    context = {'title': 'Главная страница',
               'apps': {'blog': views.side_bar['side_bar'], 'discussions': 'form', },
               'request': request}

    return render(request, 'templates_project/base.html', context=context)
