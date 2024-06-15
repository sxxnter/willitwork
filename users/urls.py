"""Определяет URL адреса для users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Шаблон выхода из аккаунта
    path('logout/', views.logout_view, name='logout'),
    # Включение ссылок аутентификации
    path('', include('django.contrib.auth.urls')),
    # Страница для регистрации аккаунта
    path('register/', views.register, name='register'),
]