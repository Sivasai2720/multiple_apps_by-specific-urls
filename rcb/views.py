from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kholi(request):
    return render(request,'kholi.html')


def abd(request):
    return HttpResponse('<h1>Super Bater Mr.ABD</h1>')