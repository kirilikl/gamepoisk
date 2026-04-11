from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('game_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки ниже.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})