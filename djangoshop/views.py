import os
from .settings import BASE_DIR
from .forms import AuthUserForm
from django.shortcuts import render
from blog import views
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

app_name_path = os.path.join(BASE_DIR, '')

apps = {'blog': views.side_bar['side_bar']}

def home_view(request):
    context = {'title': 'Главная страница',
               'apps': apps,
               'request': request}

    return render(request, 'templates_project/base.html', context=context)


class LoginPageView(LoginView):
    template_name = 'templates_project/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {'title': 'Авторизация', 'apps': apps}
        return dict(list(context.items()) + list(c_def.items()))