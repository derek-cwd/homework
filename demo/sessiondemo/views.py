from django.shortcuts import render
from django.http import HttpResponse


def setsessionfunc(request):

    request.session['itcast123'] = 'python123'

    return HttpResponse('setsessionfunc')


def getsessionfunc(request):

    value = request.session['itcast123']

    print(value)

    return HttpResponse('getsessionfunc')