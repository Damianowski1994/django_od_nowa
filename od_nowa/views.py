# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.http.response import HttpResponse


def test(request):
    return HttpResponse("siema siema byku!!!")