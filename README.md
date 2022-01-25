Подготовка проекта:
- создать проект django-admin startproject
- добавить библиотеки в requirements.txt (django 4)
- добавить environ https://github.com/joke2k/django-environ
- добавить psycopg2-binary
- создать базу данных

Подготовка модели пользователя:
- создать приложение core
- зарегистрировать модель User, добавить в settings AUTH_USER_MODEL
- создать миграцию пользователя 
- накатить миграции

Регистрация:
- поставить drf
- добавить urls в core
- написать Serializer для пользователя
- написать view

Вход:
- разобраться с auth backends
- реализовать login

Профиль:
- класс RetrieveUpdateDestroyAPIView
- get текущий профиль
- post обновить 
- delete логаут 

Обновить пароль:
- стандартные django валидаторы пароля
- UpdateAPIView

Social auth:
- https://python-social-auth.readthedocs.io/en/latest/configuration/django.html 
- https://dev.vk.com/api/oauth-parameters
- https://python-social-auth.readthedocs.io/en/latest/backends/vk.html
- auth url: 127.0.0.1:8000/oauth/login/vk-oauth2
- Настроить перенаправления https://python-social-auth.readthedocs.io/en/latest/configuration/settings.html?highlight=success#urls-options
- https://python-social-auth.readthedocs.io/en/latest/configuration/django.html#exceptions-middleware
- SocialAuthExceptionMiddleware (убрать debug)
