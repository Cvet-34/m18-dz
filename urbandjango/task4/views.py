from django.shortcuts import render


# Create your views here.
def menu(request):
    text = 'Природные товары для красоты издоровья!'
    list = ['надежная упаковка', 'высокое качество продукции', 'вся продукция сертифицирована']
    context = {
        'text': text,
        'list': list
        }
    return render(request, 'fourth_task\menu.html', context)


def platform(request):
    return render(request, 'fourth_task\platform.html')


def games(request):
    title = 'КАТОЛОГ ТОВАРОВ'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task\games.html', context)


def base(request):
    return render((request, 'platform.html'))