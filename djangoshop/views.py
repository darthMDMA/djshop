import os
from .settings import BASE_DIR
from django.shortcuts import render
import re

app_name_path = os.path.join(BASE_DIR, '')


def home_view(request):
    context = {'title': 'Главная страница', 'apps': {}}

    for app in os.listdir(app_name_path):
        if app in os.listdir(BASE_DIR):
            models_file_path = os.path.join(BASE_DIR, f'{app}\models.py')
            try:
                with open(models_file_path, mode='r', encoding='utf-8') as file:
                    data = file.read().replace('\n', '')
                    patern = re.findall(r"(?<=\bverbose_name = ')[а-яА-Я ]+", data)
                    if app in context['apps']:
                        context['apps'].get(app, patern)
                    else:
                        context['apps'][f'{app}'] = patern
            except:
                pass

    return render(request, 'templates_project/base.html', context=context)
