from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.





def setcookfunc(request):
    '设置cookie'

    # 1. 创建response
    response = HttpResponse('setcookfunc')

    response.set_cookie('itcast', 'python', max_age=3600)

    return response


def getcookfunc(request):

    value = request.COOKIES.get('itcast')

    print(value)

    return HttpResponse('getcookfunc')