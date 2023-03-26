from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "name": "Roshan",
        "age": 23,
        "marks": [23, 45, 56, 78]
    }
    return render(request, "index.html", context)

# def about(request):
#     return HttpResponse('<h1>About</h1>')

def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "other/contact.html")