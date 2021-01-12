from django.shortcuts import render
from .models import Jag, Todo
from .fome import Ja


def home(res):
    if res.method == 'POST':
        a = Ja(res.POST,res.FILES)
        if a.is_valid():
            a.save()
    else:
        a = Ja()
    return render(res, 'new/jag.html', {'a': a})


# Create your views here.
