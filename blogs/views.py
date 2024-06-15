from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """Домашняя страница blog"""
    return render(request, 'blogs/index.html')

@login_required
def notes(request):
    """Выводит список заметок"""
    notes = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
    context = {'notes': notes}
    return render(request, 'blogs/notes.html', context)

@login_required
def new_note(request):
    """Создает новую заметку"""
    if request.method != 'POST':
        # Данные не отправлялись; создается новая заметка
        form = BlogForm()
    else:
        # Данные отправлены; обработать их
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            return redirect('blogs:notes')
    
    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'blogs/new_note.html', context)

@login_required
def edit_note(request, note_id):
    """Редактирование заметки"""
    # Получает объект заметки.
    note = BlogPost.objects.get(id=note_id)
    
    _check_note_owner(request, note)

    # Вывод заметки с хранящимися в ней данными
    if request.method != 'POST':
        form = BlogForm(instance=note)
    else:
        # Данные отправлены; обработать их
        form = BlogForm(instance=note, data=request.POST)
        if form.is_valid():
            edit_note = form.save(commit=False)
            edit_note.owner = request.user
            edit_note.save()
            return redirect('blogs:notes')
    
    # Вывести пустую или недействительную форму
    context = {'note': note, 'form': form}
    return render(request, 'blogs/edit_note.html', context)

def _check_note_owner(request, note):
    """Проверка того, что тема принадлежит текущему пользователю"""
    if note.owner != request.user:
        raise Http404