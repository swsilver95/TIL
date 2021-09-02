from django.shortcuts import render
from .calc_date import dday

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')


def getdate(request):
    return render(request, 'articles/getdate.html')


def result(request):
    date = request.GET.get('date')
    context = dday(date)
    return render(request, 'articles/result.html', context)