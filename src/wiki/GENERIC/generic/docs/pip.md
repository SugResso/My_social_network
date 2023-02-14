[Django](https://www.djangoproject.com/download/)

`pip install django`

```

```

[django-cleanup](https://pypi.org/project/django-cleanup/)

`pip install django-cleanup`

```

```

[pillow](https://pypi.org/project/Pillow/)

`pip install pillow`

```

```

## Настройка ckeditor

[django-ckeditor](https://pypi.org/project/django-ckeditor/)

`pip install django-ckeditor`

```python

CKEDITOR_CONFIGS = {
    'default': {
        'width': 'auto'
    }
}
# после python manage.py collectstatic
```

## Настройка django-allauth

[django-allauth](https://django-allauth.readthedocs.io/en/latest/)

`pip install django-allauth`

```python
INSTALLED_APPS = [
    # django.contrib.sites обязательно после django.contrib.messages
    'django.contrib.sites',
]

SITE_ID = 1

CKEDITOR_CONFIGS = {
    'default': {
        'width': 'auto'
    }
}
# после python manage.py collectstatic
```

## Настройка dotenv

[dpython-dotenv](https://pypi.org/project/python-dotenv/)

`pip install dpython-dotenv`

```python

# .env в корне проекта(src/.env)
from dotenv import load_dotenv

# Loading ENV
env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)
```

## Настройка django-braces

[django-braces](https://pypi.org/project/django-braces/)

`pip install django-braces`

```python


```

[channels](https://pypi.org/project/channels/)

`python -m pip install -U channels`

```


```

[mkdocs](https://pypi.org/project/mkdocs/)

`pip install mkdocs`

```

```

[mkdocs-awesome-pages-plugin](https://pypi.org/project/mkdocs-awesome-pages-plugin/)

`pip install mkdocs-awesome-pages-plugin`

```

```

[mkdocs-material](https://squidfunk.github.io/mkdocs-material/getting-started/)

`pip install mkdocs-material`

```

```

[django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

`python -m pip install django-debug-toolbar`

```

```

[//]: # ([]&#40;&#41;)

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # (`pip install mkdocs`)

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # (```)

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # (```)