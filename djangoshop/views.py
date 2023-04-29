import os
from .settings import BASE_DIR
from .forms import AuthUserForm, RegisterUserForm
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.shortcuts import render
from blog import views
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.contrib import messages

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


class RegisterPageView(CreateView):
    template_name = 'templates_project/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_url')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {'title': 'Регистрация', 'apps': apps}
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):  # метод вызывается при успешной проверки формы регистрации и автоматически логинит пользователя
        user = form.save()  # добавляем пользователя в базу данных
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)  # вызоф функции джанго, которая авторизовывает пользователя
        return redirect('login_url')  #


def logoutuser(request): # функция разлогинивания
    logout(request) # вызываем  стандартную функцию джанго logout
    return redirect('login_url') # выполняем перенаправление на нужную страницу