from django.shortcuts import render
from django.http import HttpResponse
from .forms import Name_Form

def home(request):
    if request.method == 'POST':
        form = Name_Form(request.POST)
        if form.is_valid():
            return render(request, 'home.html', {'name': form.cleaned_data['name_input']})
    else:
        form = Name_Form()
    return render(request, 'home.html', {'form': form})

def profile(request):
    return render(request,'profile.html')
def key(request):
    return render(request,'key.html')
def this_week(request):
    return render(request,'thisweek.html')
def today(request):
    return render(request,'today.html')
