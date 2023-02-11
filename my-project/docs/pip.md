## Настройка mkdocs

[mkdocs](https://www.mkdocs.org/getting-started/)

`pip install mkdocs`

`mkdocs serve`

```python
```

## Настройка dotenv

[dotenv](https://pypi.org/project/python-dotenv/)

`pip install dotenv`

```python
from dotenv import load_dotenv
# Loading ENV
env_path = Path('.') / '.env'
# env_path = '.env'
load_dotenv(dotenv_path=env_path)
```

## Настройка django-allauth

[django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

`pip install django-allauth`

в settings.py

```python
INSTALLED_APPS = [
    ...
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    ...
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
```
в urls.py
```python
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```
## Настройка debug_toolbar

[debug_toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

`python -m pip install django-debug-toolbar`

в settings.py
```python
INSTALLED_APPS = [
    # ...
    "django.contrib.staticfiles",
    # ...
    "debug_toolbar",
    # ...
]

STATIC_URL = "static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        # ...
    }
]

MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
```

в urls.py
```python
from django.urls import include, path

urlpatterns = [
    # ...
    path('__debug__/', include('debug_toolbar.urls')),
]
```

## Настройка debug_channels
[channels](https://channels.readthedocs.io/en/stable/installation.html)

`python -m pip install -U channels`

в settings.py
```python
ASGI_APPLICATION = "myproject.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
```
## Установка jupyter notebook

[jupyter notebook](https://jupyter.org/install)
[django-extensions](https://gist.github.com/EtsuNDmA/85a20b0b8cf5ec4e12352507b14f9762)

`pip install notebook`
`pip install django-extensions`

в settings.py

```python
INSTALLED_APPS = (
    ...
    'django_extensions',
)
```



## Настройка django-taggit

[django-taggit](https://django-taggit.readthedocs.io/en/latest/getting_started.html)

`pip install django-taggit`

```python
Add "taggit" to your project’s INSTALLED_APPS setting.
```

## Настройка pillow

[pillow](https://django-crispy-forms.readthedocs.io/en/latest/install.html)

`pip install pillow`

```python
Какой то код
```
## Настройка django-cleanup

[django-cleanup](https://github.com/un1t/django-cleanup?ysclid=ld4z38aeff981787259)

`pip install django-cleanup`

```python
Какой то код
```


