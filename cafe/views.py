from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def main_page(request):
    return HttpResponse("Hello, Honey !")


def test_view(request):
    number = 1000
    return HttpResponse(number)

