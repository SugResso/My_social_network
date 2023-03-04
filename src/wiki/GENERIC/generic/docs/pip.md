## Команды Django 4.1.6

[Django](https://www.djangoproject.com/download/)

`pip install django` - установить

`django-admin startproject name_project` - создать проекта

`python manage.py startapp name_app` - создать приложения

`python manage.py createsuperuser` - создать супер пользователя

`python manage.py makemigrations` - провести миграции

`python manage.py migrate` - применить миграции

`python manage.py collectstatic` - собрать статику

`python manage.py runserver` - запуск


## Настройка cleanup 6.0.0

[django-cleanup](https://pypi.org/project/django-cleanup/)

`pip install django-cleanup` - установить

```
INSTALLED_APPS = (
    ...,
    'django_cleanup.apps.CleanupConfig',
)
```


## Настройка pillow 9.4.0

[pillow](https://pypi.org/project/Pillow/)

`pip install pillow` - установить


## Настройка ckeditor 6.5.1

[django-ckeditor](https://pypi.org/project/django-ckeditor/)

`pip install django-ckeditor` - установить

```
INSTALLED_APPS = (
    ...,
    # должна быть последней
    'django_cleanup.apps.CleanupConfig',
)

CKEDITOR_CONFIGS = {
    'default': {
        'width': 'auto'
    }
}
```

После настройки собрать статику:

    python manage.py collectstatic


## Настройка allauth 0.52.0

[django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

`pip install django-allauth` - установить

```
INSTALLED_APPS = [
    # django.contrib.sites обязательно после django.contrib.messages
    'django.contrib.sites',
]

SITE_ID = 1
``` 
Провести миграции:

    python manage.py makemigrations
    python manage.py migrate

```
INSTALLED_APPS = [
    # после django.contrib.sites
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}

urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```


## Настройка dotenv 0.21.1

[dpython-dotenv](https://pypi.org/project/python-dotenv/)

`pip install dpython-dotenv` - установить

```
# .env в корне проекта(src/.env)
from dotenv import load_dotenv

# Loading ENV
env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)
```


## Настройка braces 1.15.0

[django-braces](https://pypi.org/project/django-braces/)

`pip install django-braces` - установить


## Настройка channels 4.0.0

[channels](https://channels.readthedocs.io/en/stable/installation.html)

`python -m pip install -U channels` - установить

```
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    ...
    'channels',
)

ASGI_APPLICATION = 'godot_social_network.routing.application'

CHANNELS_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}
```


## Настройка mkdocs 1.4.2

[mkdocs](https://pypi.org/project/mkdocs/)

`pip install mkdocs` - установить

```

```

[mkdocs-awesome-pages-plugin](https://pypi.org/project/mkdocs-awesome-pages-plugin/)

`pip install mkdocs-awesome-pages-plugin` - установить

```

```

[mkdocs-material](https://squidfunk.github.io/mkdocs-material/getting-started/)

`pip install mkdocs-material` - установить

```

```


## Настройка debyg toolbar 3.8.1

[django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

`python -m pip install django-debug-toolbar` - установить

```
INSTALLED_APPS = [
    # ...
    "debug_toolbar",
    # ...
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
В urls.py:

    if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__dubug__/', include(debug_toolbar.urls))
                  ] + urlpatterns


## Настройка jupyter

[jupyter notebook](https://jupyter.org/install)

`pip install notebook` - установить

`python manage.py shell_plus --notebook` - запуск

```
INSTALLED_APPS = (
    ...
    'django_extensions',
)
```

## Настройка nbextensions

[Jupyter](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)

`pip install jupyter_contrib_nbextensions` - установить

`jupyter contrib nbextension install --user`

```
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
```
Теперь нужно запустить jupyter, если у вас вверху нет раздел Nbextensions, то пропишем ещё одну команду:
```
jupyter contrib nbextension install --user --skip-running-check
```

## Настройка taggit

[Taggit](https://django-taggit.readthedocs.io/en/latest/getting_started.html)

`pip install django-taggit` - установить

```

```