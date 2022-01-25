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
