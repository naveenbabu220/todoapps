from django.shortcuts import render
from .models import User
from .froms import Ufr

# Create your views here.

def user(rep):
    if rep.method == "POST":
        a = Ufr(rep.POST, rep.FILES)
        if a.is_valid():
            a.save()
    else:
        a = Ufr()
    return render(rep,'user/usr.html' ,{'a':a})