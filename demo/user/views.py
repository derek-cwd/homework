from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.urls import reverse


def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """

    print('hello world 函数')

    return HttpResponse('hello world!')


def say(request):

    print('hahaha')

    return HttpResponse('hahahaha')


def sayhello(request):
    print('hello')

    return HttpResponse('hello')

def rev(request):

    url = reverse('user:index')



    print(url)

    # return HttpResponse('rev')

    return redirect(url)