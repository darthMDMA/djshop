from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': forms}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': forms}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': forms}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': forms}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') # поля отображения