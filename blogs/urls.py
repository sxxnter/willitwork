"""Определяет URL адреса для blogs"""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница заметок
    path('notes/', views.notes, name='notes'),
    # Добавление заметки
    path('new_note/', views.new_note, name='new_note'),
    # Редактирование заметки
    path('edit_note/<int:note_id>', views.edit_note, name='edit_note'),
]