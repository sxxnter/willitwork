from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        # Данные не отправлялись; создается новая заметка
        form = UserCreationForm()
    else:
        # Данные отправлены; обработать данные
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogs:index')
    
    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'users/register.html', context)

def logout_view(request):
    """Выход из аккаунта пользователя"""
    if request.method == 'POST':
        logout(request)
        
    return render(request, 'users/logged_out.html')