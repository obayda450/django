from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")


def great(request, name):
    return render(request, "hello/great.html", {
        "name": name
        })
