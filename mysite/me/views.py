from django.shortcuts import render , redirect
from .models import *
from .forms import HomeForm

# Create your views here.

def home(request):
    info = Info.objects.all()
    about = Aboutme.objects.all()
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('number') and request.POST.get('messages'):
            saverecord = HomeForm()
            saverecord.name = request.POST.get('name')
            saverecord.email = request.POST.get('email')
            saverecord.number = request.POST.get('number')
            saverecord.messages = request.POST.get('messages')
            saverecord.save()

    return render(request , "me/index.html" , {"info" : info , "about" : about})