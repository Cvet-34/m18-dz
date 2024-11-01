from django.shortcuts import render
from django.shortcuts import render
from .forms import UserRegister




# Create your views here.
def registration_page(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            #Обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']


    else:


        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})




