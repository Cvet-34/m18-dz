from django.shortcuts import render

# Create your views here.
def platform(request):
    title = 'ПРИРОДНЫ ТОВАРЯ ДЛЯ ЗДОРОВЬЯ'
    text = 'ДОБРО ПОЖАЛОВАТЬ!'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task\platform.html', context)

def games(request):
    title = 'КАТОЛОГ ТОВАРОВ'
    context = {
        'title': title,
    }
    return render(request, 'third_task\games.html', context)