<h1 align="center"> About_photographer </h1>

<p align="center">
<--<a href="https://github.com/SugResso/SugResso"> прошлый проект </a>
|
<a href="https://github.com/SugResso/task_book"> следующий проект </a> -->
</p>

---

### Первый коммит - создание проекта

- Установка библиотек:

        pip install django
        pip install django-cleanup pillow django-ckeditor django-allauth python-dotenv django-braces 
        python -m pip install -U channels
        pip install mkdocs
- Создадим проект, название директорий взял с этого <a href="https://www.youtube.com/watch?v=LPo29ygf0wA&t=158s">
  видео</a>

        django-admin startproject src
  в папке [src](src) переименовываем папку src на [config](src/config)

---

### Второй коммит - создаем документацию к проекту

#### Примечание: если вы шарите за GitBook то можете сделать всё, то же самое на нём. Я этого делать не буду, т.к. повторяю за автором курса, но в будущем обязательно попробую.

- Автор курса предлагает создать директорию с таким путем к ней, такая глубина вложенности объясняется тем, что
  понадобится в будущем.
  находясь в папке [src](src), пропишем команду:

        mkdocs new wiki
- В созданной папке [wiki](src/wiki) нужно создать папки, чтобы получился такой путь

      wiki/GENERIC/generic
  теперь перенесём всё её содержимое из [wiki](src/wiki)(кроме [GENERIC](src/wiki/GENERIC)) в
  папку [generic](src/wiki/GENERIC/generic) и создадим папку [wiki](src/wiki/GENERIC/generic/wiki), и в
  папке [docs](src/wiki/GENERIC/generic/docs) 3
  файла([dev.md](src/wiki/GENERIC/generic/docs/dev.md), [index.md](src/wiki/GENERIC/generic/docs/index.md), [settings.md](src/wiki/GENERIC/generic/docs/settings.md), [pip.md](src/wiki/GENERIC/generic/docs/pip.md)).


- В файле [mkdocs.yml](src/wiki/GENERIC/generic/mkdocs.yml) нужно продублировать следующий код

      site_name: About_photographer

      site_dir: 'wiki/GENERIC/generic/build'


      nav:
        - index: index.md
        - pip install: pip.md
        - Dev: dev.md
        - settings: settings.md
        - Blog: blog/models.md

      theme:
        name: material


      dev_addr:
        127.0.0.1:8200


      markdown_extensions:
        - pymdownx.highlight
        - pymdownx.inlinehilite
        - pymdownx.superfences
        - pymdownx.snippets
        - toc:
            permalink: True


      collapse_single_pages: true

      plugins:
        - search
        - awesome-pages

      site_author:
        Ваша фамилия и имя


- В папке [generic](src/wiki/GENERIC/generic) пропишем следующие команды:

      pip install mkdocs-awesome-pages-plugin
      pip install mkdocs-material
      mkdocs build

### Проверь себя:

Вторая часть на этом подошла к концу, если вы всё сделали правильно, тогда введите команду

      mkdocs serve

Если вы всё делали правильно, то увидите такое сообщение

    WARNING  -  Config value 'collapse_single_pages': Unrecognised configuration name: collapse_single_pages
    INFO     -  Building documentation...
    INFO     -  Cleaning site directory
    INFO     -  The following pages exist in the docs directory, but are not included in the "nav" configuration:
                  - blog\templates.md
                  - blog\urls.md
                  - blog\view.md
    INFO     -  Documentation built in 0.36 seconds
    INFO     -  [15:17:05] Watching paths for changes: 'docs', 'mkdocs.yml'
    INFO     -  [15:17:05] Serving on http://127.0.0.1:8200/

По ссылке у вас откроется [сайт](http://127.0.0.1:8200/) с документацией
![img.png](img/c2_mkdocs_1.png)
---

### Третий коммит - Настроим статику, создаем бд и создаем супер пользователя

- Укажем кодировку в файле [settings.py](src/config/settings.py), для того чтобы мы могли писать русские символы. Для
  этого нужно разместить в первой строке вот эту строку:

      # -*- coding: utf-8 -*-

  Нужно вставить этот код после переменной ```STATIC_URL = 'static/'```, сразу прикрепляем ссылки на ресурсы по данным
  разделам и комментируем их.

      # https://docs.djangoproject.com/en/4.0/ref/settings/#static-root
      STATIC_ROOT = os.path.join(BASE_DIR, 'static')

      # https://docs.djangoproject.com/en/4.0/ref/settings/#staticfiles-dirs
      STATICFILES_DIRS = [
      
          # os.path.join(BASE_DIR, "my_site/templates"),
      
      ]
      
      # https://docs.djangoproject.com/en/4.0/ref/settings/#staticfiles-finders
      STATICFILES_FINDERS = [
          "django.contrib.staticfiles.finders.FileSystemFinder",
          "django.contrib.staticfiles.finders.AppDirectoriesFinder",
      ]

  Немного о каждом из разделов:
  STATIC_ROOT - показываем путь к папке [static](src/static)
  STATICFILES_DIRS - прописываем путь к статике которая лежит где-то помимо папки [static](src/static)
  STATICFILES_FINDERS - тут расположены две утилиты по поиску статики, первая будет искать по пути из STATICFILES_DIRS,
  а вторая в подкаталогах приложений
  <br>
  <br>
  Также в файле [settings.py](src/config/settings.py) меняем значение переменной, в ней мы указываем хост, '*' означает,
  что мы выбрали все хосты.

      ALLOWED_HOSTS = ['*']

- теперь из папки [src](src) пропишем такую команду:

      python manage.py collectstatic
  после чего у вас должна появится папка [static](src/static).

- В файле [urls.py](src/config/urls.py) добавим, как и в [settings.py](src/config/settings.py), такую строку(также
  первой строкой):

      # -*- coding: utf-8 -*-

  В конце вставьте:

      if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  чтобы это работало добавляем два импорта:

      from django.conf.urls.static import static
      from django.conf import settings

- вернемся в [settings.py](src/config/settings.py) и добавим путь к медиафайлам, но сперва создадим
  папку [media](src/media):

      #https://docs.djangoproject.com/en/4.0/ref/settings/#media-root
      MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        
      #https://docs.djangoproject.com/en/4.0/ref/settings/#media-url
      MEDIA_URL = '/media/'
  Буду стараться не забывать оставлять комментарии со ссылками по каждому разделу, если я что-то не объяснил, то у вас
  будет возможность перейти по ссылке.

- Создадим базу данных, по умолчанию это SQLite, но чуть позже заменим на PostgreSQL:

      python manage.py makemigrations
      python manage.py migrate

- Создадим суперпользователя:

      python manage.py createsuperuser
  Далее заполняете данные, Username это будущий логин в админку, почта не обязательна(просто нажимаете Enter), при вводе
  пароль не отображается хоть вы его и вводите

      Username (leave blank to use 'ixolm'): 
      Email address: 
      Password: 
      Password (again):
      This password is too short. It must contain at least 8 characters.
      This password is entirely numeric.
      Bypass password validation and create user anyway? [y/N]: y
      Superuser created successfully.
  ![c3_cmd_1.png](img/c3_cmd_1.png)

### Проверь себя:

Введите команду:

      python manage.py runserver

Для выключения в терминале нажмите "Ctrl + C"

Последней строкой вы увидите адрес вашего сайта, туда и перейдём, нас встретит такая страница:

![c3_web_1.png](img/c3_web_1.png)

Теперь перейдем в админку, для это ```http://127.0.0.1:8000/admin```

![c3_web_admin_1.png](img/c3_web_admin_1.png)

Вводим данные, которые указали при регистрации супер пользователя и всё, вы в админке.

![c3_web_admin_2.png](img/c3_web_admin_2.png)

---

### Четвёртый коммит - создаем приложение

- В дальнейшем нам понадобится хранить шаблоны, их принято хранить в папке ```templates```, но для неё нужно указать
  путь, это мы делаем в переменной ```DIRS```:

      TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [os.path.join(BASE_DIR, 'templates')],
              'APP_DIRS': True,
              'OPTIONS': {
                  'context_processors': [
                      'django.template.context_processors.debug',
                      'django.template.context_processors.request',
                      'django.contrib.auth.context_processors.auth',
                      'django.contrib.messages.context_processors.messages',
                  ],
              },
          },
      ]
- Создать приложение очень просто, нужно прописать одну команду из папки [src](src):

      python manage.py startapp blog
  blog - это название будущего приложения.

  Чтобы django знала об этом приложении, его нужно указать в файле [settings.py](src/config/settings.py) в
  переменной ```INSTALLED_APPS```:

      INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
      
          'blog.apps.BlogConfig', 
      ]
  вы могли видеть, что указывают только название приложения, но с полным путём django не будет искать во всём
  приложении, а уже будет точно знать к чему обращаться.


- Мы уже скачивали библиотеку django-cleanup, теперь мы её подключим, для этого нужно добавить следующие строки в
  переменную ```INSTALLED_APPS```:

      # должна быть последней
      # https://github.com/un1t/django-cleanup
      'django_cleanup.apps.CleanupConfig',

  Сразу добавим ещё одну библиотеке, для красивого отображения форм(регистрации, отзывов и т.д.):

      'crispy_forms',
  её можно расположить сразу после ```django.contrib.staticfiles```. Для неё есть ещё настройка, которую мы расположим в
  конце файла [settings.py](src/config/settings.py):

      # django-crispy-forms
      # https://django-crispy-forms.readthedocs.io/en/latest/install.html

      CRISPY_TEMPLATE_PACK = 'uni_form'
      
      # End django-crispy-forms
  Первым и последним комментарием мы отделяем блок настроек, в данном случае для ```django-crispy-forms```

- У нас есть переменные, которые нежелательно хранить в открытом коде и вообще лучше некоторые данные хранить отдельно
  для этого мы воспользуемся библиотекой ```dotenv```, в файле [settings.py](src/config/settings.py) вставляем такой
  код:

      from django.contrib.messages import constants as messages

      # python-dotenv
      # https://pypi.org/project/python-dotenv/
      from dotenv import load_dotenv
      # Loading ENV

      env_path = Path('.') / '.env'
      
      load_dotenv(dotenv_path=env_path)

      # End python-dotenv

  В паке [src](src) создадим папку ```.env```, затем копируем переменную ```SECRET_KEY```
  из [settings.py](src/config/settings.py) в ```.env```:

      SECRET_KEY = 'какой-то пароль' 
  В [settings.py](src/config/settings.py) нужно заменить значение переменной ```SECRET_KEY``` на:

      SECRET_KEY = os.getenv('SECRET_KEY')

### Проверь себя:

Всё тоже что и в прошлый раз.

Введите команду:

      python manage.py runserver

Для выключения в терминале нажмите "Ctrl + C"

Результат должен быть, как и в прошлый раз.

---

### Пятый коммит - django-ckeditor, django.contrib.sites, django-allauth

- Добавим `'ckeditor',` в `INSTALLED_APPS`(файл [settings.py](src/config/settings.py)) после `crispy_forms`. После нужно
  спуститься в самый низ этого файла и вставить это:

      # django-ckeditor
      # https://pypi.org/project/django-ckeditor/
      CKEDITOR_CONFIGS = {
          'default': {
              'width': 'auto'
          }
      }
      
      # End django-ckeditor

  После этого нужно собрать статику, для этого пропишем команду:

      python manage.py collectstatic
  После чего должна появится папка `ckeditor` в папке [static](src/static)

- Добавим библиотеку для хранения доменных имен и «подробных» имен ваших сайтов в `INSTALLED_APPS`(
  файл [settings.py](src/config/settings.py))
  после `'django.contrib.messages'` вставим `'django.contrib.sites',`. Для её работы нужно прописать `SITE_ID`
  после `INSTALLED_APPS`:

      SITE_ID = 1
  После нужно провести миграции:

      python manage.py makemigrations
      python manage.py migrate

  Теперь нужно зайти в адмику, как в конце третьего раздела, у вас появится раздел Sites, нажимаем на него, у вас будет
  так:
  ![img.png](img/c5_web_admin_1.png)
  Перейдем в `example.com` и заменим поля на `127.0.0.1:8000`
  ![img.png](img/c5_web_admin_2.png)

- Добавим библиотеку для аутентификации `django-allauth`, пропишем `AUTHENTICATION_BACKENDS`(
  файл [settings.py](src/config/settings.py)) после переменной TEMPLATES:

      # django-allauth
      # https://django-allauth.readthedocs.io/en/latest/
      
      AUTHENTICATION_BACKENDS = [
          'django.contrib.auth.backends.ModelBackend',
          'allauth.account.auth_backends.AuthenticationBackend',
      ]
      
      # End django-allauth
  В `INSTALLED_APPS` пропишем следующие после `'django.contrib.staticfiles'`:

      'allauth',
      'allauth.account',
      'allauth.socialaccount',
      'allauth.socialaccount.providers.google',
      'allauth.socialaccount.providers.github',
  [urls.py](src/config/urls.py) первой строкой добавим `from django.conf.urls import include`, в
  переменной `urlpatterns`
  последней строкой добавим следующее:

      path('accounts/', include('allauth.urls')),
  Проведем миграции:

      python manage.py makemigrations
      python manage.py migrate

  Добавим социальных провайдеров после `AUTHENTICATION_BACKENDS`:

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

### Проверь себя:

Заходим в адмику и сравниваем со скрином ниже:

      python manage.py runserver

Для выключения в терминале нажмите "Ctrl + C"

![img.png](img/c5_web_admin_3.png)

---

### Шестой коммит - contrib.humanize, debug_toolbar

- Добавим библиотеку `django.contrib.humanize` в `INSTALLED_APPS`(файл [settings.py](src/config/settings.py))
  после `'django.contrib.staticfiles'`:

      # https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/
      'django.contrib.humanize',

- Установим новую библиотеку `django-debug-toolbar`:

      python -m pip install django-debug-toolbar
  Добавляем в `INSTALLED_APPS`(файл [settings.py](src/config/settings.py)) после `'django.contrib.staticfiles'`:

      #https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
      'django-debug-toolbar',
  Добавляем в `MIDDLEWARE` последней строкой `'debug_toolbar.middleware.DebugToolbarMiddleware', # django-debug-toolbar`
  В [urls.py](src/config/urls.py) последней строкой добавим следующее:

      if settings.DEBUG:
      import debug_toolbar

      urlpatterns = [
                        path('__dubug__/', include(debug_toolbar.urls))
                    ] + urlpatterns
  Проведем миграции:

      python manage.py collectstatic

### Проверь себя:

Запускаем сервер, если всё работает и можете зайти в адмику, то переходите к следующему шагу.

      python manage.py runserver

Для выключения в терминале нажмите "Ctrl + C"

---

### Седьмой коммит - pip.md, channels

- Добавляем в `INSTALLED_APPS`(файл [settings.py](src/config/settings.py)) после `'debug_toolbar'`:

      # https://channels.readthedocs.io/en/stable/installation.html
      # 'channels',
  В конце файла добавляем блок настроек:

      # django-channels
      # https://channels.readthedocs.io/en/stable/installation.html
      """
      ASGI_APPLICATION = 'config.routing.application'
      
      CHANNELS_LAYERS = {
          'default': {
              'BACKEND': 'channels.layers.InMemoryChannelLayer'
          }
      }
      """
      # End django-channels
  Можете заметить что всё закомментировано, потому что пригодиться в будущем, а сейчас будет мешать.
  Создадим [routing.py](src/config/routing.py) и поместим в него следующее:

      from channels.auth import AuthMiddlewareStack
      from channels.routing import ProtocolTypeRouter, URLRouter
      # import chat.routing
      
      application = ProtocolTypeRouter({
          'websocket': AuthMiddlewareStack(
              URLRouter(
                  #chat.routing.websocket_urlpatterns
              )
          ),
      })

### Проверь себя a.k.a. Примечание:

Коммиты стали гораздо короче и буду такими оставаться. По поводу блока "Проверь себя", если его нет, то значит он
соответствует ниже указанному.

1) Провести миграции:

        python manage.py makemigrations
2) Применить миграции:

        python manage.py migrate
3) Собрать статику:

        python manage.py collectstatic
4) Запускаем сервер, если всё работает и можете зайти в адмику, то переходите к следующему шагу.

       python manage.py runserver

Для выключения в терминале нажмите "Ctrl + C"

1-3 пункты я говорю когда нужно сделать, но если у вас что-то не работает, то пробуйте выполнить эти пункты. Их можно
делать бесконечно, ничего лишнего вы не создадите.

---

### Восьмой коммит - EMAIL, MESSAGE

- Прописываем недостающие настройки в самом низу файла [settings.py](src/config/settings.py)

      # email

      EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
      EMAIL_HOST = 'smtp.gmail.com'
      EMAIL_PORT = os.getenv('EMAIL_PORT')
      EMAIL_USE_TLS = True
      EMAIL_HOST_USER = os.getenv('EMAIL_USER')
      EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASS')
      
      # End email

      GOOGLE_RECAPTCHA_SECRET_KEY = os.getenv('GOOGLE_RECAPTCHA_SECRET_KEY')

      MESSAGE_TAGS = {
          messages.DEBUG: 'alert-secondary',
          messages.INFO: 'alert-info',
          messages.SUCCESS: 'alert-success',
          messages.WARNING: 'alert-warning',
          messages.ERROR: 'alert-error',
      }

  Добавим переменные в файл .env:

      DEBUG=True
      EMAIL_USER=your_email@mail.ru
      EMAIL_PASS=email_password
      EMAIL_PORT=587
      GOOGLE_RECAPTCHA_SECRET_KEY = 

---

### Девятый коммит - jupyter-notebook

- установка jupyter-notebook:

      pip install notebook
  установка django-extensions

      pip install django-extensions

  Добавляем в `INSTALLED_APPS`(файл [settings.py](src/config/settings.py)) после `'django.contrib.humanize'`:

      # https://django-extensions.readthedocs.io/en/latest/installation_instructions.html
      'django_extensions',
  Собираем статику:

      python manage.py collectstatic

  Команда для запуска jupyter:

            python manage.py shell_plus --notebook
  Для выключения в терминале нажмите "Ctrl + C"

  В [settings.py](src/config/settings.py) пропишем следующее в самом низу:

      os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'

---

### Десятый коммит - customization jupyter

- В [models.py](src/blog/models.py) создадим модель:

      class Post(models.Model):
          title = models.CharField(max_length=200)

  Проведем миграции:

      python manage.py makemigrations
      python manage.py migrate

  Запускаем jupyter:

      python manage.py shell_plus --notebook
  Для выключения в терминале нажмите "Ctrl + C"

  Переходим New > Django Shell-Plus(Новый > Django Shell-Plus):

  ![img.png](img/c10_web_jupyter_1.png)

  Прописываем следующее:

      from django.db import models
      from blog.models import Post

      post_test_title = Post.objects.create(title='ok')
      post_test_title.title = 'super'
      post_test_title.save()
  После нажмите "Enter", если ничего не произошло, тогда "Ctrl + Enter" или "Shift + Enter", должно вывести QuerySet.

- В [admin.py](src/blog/admin.py) пропишем следующее, для более удобного отображения постов в админке:

      @admin.register(Post)
      class PageAdmin(admin.ModelAdmin):
          list_display = ['title', ]

  Заходим в адмику и проверяем, в разделе BLOG > Posts должно появится значение из QuerySet.

- Установим тему в jupyter для авто подстановки и плюсом будет темная(синяя) тема, можете поискать и поставить другую:

      pip install jupyterthemes
      jt -t chesterish
      pip install jupyter_contrib_nbextensions
      jupyter contrib nbextension install --user
      pip install jupyter_nbextensions_configurator
      jupyter nbextensions_configurator enable --user
  Теперь нужно запустить jupyter, если у вас вверху нет раздел Nbextensions, то пропишем ещё одну команду:

      jupyter contrib nbextension install --user --skip-running-check

---

### Одиннадцатый коммит - model Post

- [models.py](src/blog/models.py):

      from django.contrib.auth.models import User
      from django.utils import timezone

  в class Post

      class Meta:
          verbose_name = 'Создать пост'
          verbose_name_plural = 'Создать пост'
    
      title = models.CharField(max_length=200, help_text='до 200 символов')
      # content = models.TextField(max_length=5000, blank=True, null=True, help_text='до 5000 символов')
      date_created = models.DateTimeField(default=timezone.now)
      date_updated = models.DateTimeField(auto_now=True)
      # author = models.ForeignKey(User, on_delete=models.CASCADE)

      def __str__(self):
          return self.title

  В [migrations](src/blog/migrations) удаляем 0001 и 0002

  ![img.png](img/c11_project_migrations_1.png)

  Проведем миграции:

      python manage.py makemigrations
      python manage.py migrate

  Раскомментируем строку:

      # author = models.ForeignKey(User, on_delete=models.CASCADE)
  Проведем миграции:

      python manage.py makemigrations

  ![img.png](img/c11_project_command_1.png)
  ![img_2.png](img/c11_project_command_2.png)

      python manage.py migrate

  Раскомментируем строку:

      content = models.TextField(max_length=5000, blank=True, null=True)

  Проведем миграции:

      python manage.py makemigrations
      python manage.py migrate

### Проверь себя:

Запускаем сервер:

      python manage.py runserver

Заходим в админку, в разделе BLOG > Создать пост, удаляем все посты

![img.png](img/c11_web_admin_1.png)

Добавить пост можно справа от 'Создать пост' или выше и правее кнопки 'Go'

---

### Двенадцатый коммит - Доработка модели

- Изменим отображение в админ панели, для этого в [admin.py](src/blog/admin.py):

      list_display = ['title', 'date_created', 'date_updated', 'author', ]
- Перейдем в [models.py](src/blog/models.py) и добавим параметр для 'title':

      title = models.CharField(max_length=200, help_text='до 200 символов', db_index=True)
  Таким образом мы повышаем скорость работы поиска по полю `title`, `db_index=True` означает сохранить в кэш.
  Добавим новое поле после 'author':

      slug = models.SlugField(max_length=50, unique=True)
- Вернемся в [admin.py](src/blog/admin.py):

      prepopulated_fields = {'slug': ('title',)}
  Проведём миграции, если у вас есть какие-то посты(можете посмотреть это в админке 'BLOG' > 'Создать посты'), то лучше
  удалить, иначе нужно удалить из модели `Post` в поле `slug` настройку `unique=True`, затем:

      python manage.py makemigrations
  Будет выбор, выбираем 1, затем снова 1

      python manage.py migrate
  Если у вас были посты, то вам нужно в админке зайти в каждый пост и изменить поле `slug` так, чтобы все были разными,
  после возвращаем в поле `slug` настройку `unique=True` и проводим миграции(прошлые две команды)

Если админка выдает ошибку по добавлению/просмотру постов, то в модели `Post` закомментируем вес поля, кроме `title`
и `content`, удалим все файлы в [migrations](src/blog/migrations), кроме `__init__.py`, проведем миграции, заходим в
админку, удаляем все посты, снова удалим всё в [migrations](src/blog/migrations), кроме `__init__.py`, проведем
миграции, всё!

---

### Тринадцатый коммит - Доработка модели

- Перейдем в [models.py](src/blog/models.py) и изменим параметр для 'slug':

      slug = models.SlugField(max_length=50)  # , unique=True
  Добавим получение полного пути:

      def get_absolute_url(self):
          return reverse('post-detail', kwargs={'pk': self.pk})
  Добавим новые поля после 'slug':

      likes = models.ManyToManyField(User, related_name='postcomment', blank=True)
      reply = models.ForeignKey('self', blank=True, null=True, related_name='reply_ok', on_delete=models.CASCADE)
  После проведём миграции:

      python manage.py makemigrations
      python manage.py migrate
  Добавим подсчет лайков:

      def total_likes(self):
          return self.likes.count()

---

### Четырнадцатый коммит - Доработка модели, установка taggit

- Установим библиотеку taggit:

      pip install django-taggit
- Перейдем в [models.py](src/blog/models.py):

      from ckeditor.fields import RichTextField
  В поле `content` заменим тип поля:

      content = RichTextField(max_length=5000, blank=True, null=True, help_text='до 5000 символов')
  Проведем миграции:

      python manage.py makemigrations
      python manage.py migrate

Теперь в админке, в поле `content` будет простенький редактор текста.

---

### Пятнадцатый коммит - статика + представление

- В [src](src) создадим папку `other_static`, в ней создадим папку `bootstarp5`, в которой создаем файл `api.js`

- В [settings.py](src/config/settings.py) изменим `STATICFILES_DIRS``:

      # https://docs.djangoproject.com/en/4.0/ref/settings/#staticfiles-dirs
      STATICFILES_DIRS = [
          os.path.join(BASE_DIR, "other_static"),
      ]
  Соберем статику:

      python manage.py collectstatic
- В [src](src) создадим папку [templates](src/templates), в ней создадим
  папку [templates_projects](src/templates/templates_project), в которой создаем
  файлы [base.html](src/templates/templates_projects/base.html), [navbar.html](src/templates/templates_projects/navbar.html).
  navbar оставим пока пустым, а в base запишем следующее:

      {% include 'templates_projects/navbar.html' %}
  Пока просто в виде заготовки, никакого это функционала не несет.
- В [blog](src/blog) создадим папку [templates](src/blog/templates), в ней создадим
  папку [blog](src/blog/templates/blog), в которой создаем файлы [base.html](src/blog/templates/blog/base.html). В base
  запишем следующее:

      {% extends 'templates_projects/base.html' %}

---

### Шестнадцатый коммит - Пишем view для user и url к ней

- В [urls.py](src/config/urls.py) добавим url после `path('admin/', admin.site.urls),`:

      path('', include('blog.urls')),
- В [views.py](src/blog/views.py) пропишем класс:

      class UserPostListView(ListView):
          model = Post
    
          # template_name = ''
    
          context_object_name = 'blog_post_user_list'
      
          def get_queryset(self):
              user = get_object_or_404(User, username=self.kwargs.get('username'))
              return Post.objects.filter(author=user).order_by('-date_created')

- В [blog](src/blog) создадим `url.py` и запишем в него:

      from django.urls import path, re_path

      from views import UserPostListView
      
      
      urlpatterns = [
          path('posts/user/<str:username>/', UserPostListView.as_view(), name='user-posts-list'),
      ]

### Проверь себя:

- Войдите в админку, после переходите по данному адресу, в поле после `user/` укажите имя которое используете для входа
  в админку:

![img.png](img/c16_web_admin_1.png)

---

### Семнадцатый коммит - выводим наши посты на страницу

- В [blog](src/blog/templates/blog) создадим `user_posts.html`:

- В [views.py](src/blog/views.py) раскомментируем переменную и запишем в неё путь до `user_posts.html`:

      template_name = 'blog/user_posts.html'
- В [base.html](src/templates/templates_projects/base.html):

      <!doctype html>
      <html lang="en">
        <head>
          <!-- Required meta tags -->
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      
          <!-- Bootstrap CSS -->
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      
          <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
          {% block content %}{% endblock %}
          <!-- Optional JavaScript -->
          <!-- jQuery first, then Popper.js, then Bootstrap JS -->
          <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
          <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        </body>
      </html>
  Начальное представление взял с сайта [bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) с
  добавлением блоков в тэг `tetle` и в первую строку тэга `body`
- В [user_posts.html](src/blog/templates/blog/user_posts.html):

      {% extends 'blog/base.html' %}

      {% block title %} Post {% endblock %}
      
      {% block content %}
      <h1>Post</h1>
      {% for post in blog_post_user_list %}
      
          <h3>{{ post.title }}</h3>
      
      {% endfor %}
      
      {% endblock %}

---

### Ознакомительный коммит - templates и static

#### По поводу templates и static:
  В прошлом коммите вы могли видеть html код, в котором показано как извлекать данные для отображения на странице, с этого
  же коммита html скорее всего не будет, потому что дизаин не продуман и такой код будет занимать тут много места. Вы
  можете просто скопировать уже готовые html файлы или написать свои. Кому интересен процесс написания шаблонов(html-код),
  вы можете смотреть изменения в коммитах.(Всё это также относится к css файлам)

#### Как следить за изменениями в templates и static

1) ![img.png](img/intro1_git_1.png)
2) ![img.png](img/intro1_git_2.png)
3) ![img.png](img/intro1_git_3.png)
4) ![img_1.png](img/intro1_git_4.png)

Тут будут помечаться изменения относительно прошлого коммита.

---

### Восемнадцатый коммит - time_zone, views

- В [settings.py](src/config/settings.py) настроим время:

      TIME_ZONE = 'Europe/Moscow'
  Теперь время будет по Москве
- В [views.py](src/blog/views.py) удалим `get_queryset` и добавим на его место:

      def get_context_data(self, **kwargs):
          user = get_object_or_404(User, username=self.kwargs.get('username'))
          queryset = Post.objects.filter(author=user)
          context = super().get_context_data(**kwargs)
          context['blog_post_user_list'] = queryset.order_by('-date_created')
  
          return context