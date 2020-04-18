from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

#1.查询字符串传参



def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')

    alist = request.GET.getlist('a')

    print(a)

    print(b)

    print(alist)

    return HttpResponse('OK')


#2.通过url路径传参
def weather(request, city, year):

    print(city)

    print(year)

    return HttpResponse('weather')


#3.表单类型post
def get_body(request):

    a = request.POST.get('a')

    b = request.POST.get('b')

    alist = request.POST.getlist('a')

    print(a)

    print(b)

    print(alist)

    return HttpResponse('post_body')


#4.非表单类型的传值方式,json传参,不允许一对多,所以不可以使用getlist
import json
def get_body_json(request):

    json_bytes = request.body

    json_str = json_bytes.decode()

    dict = json.loads(json_str)

    print(dict.get('a'))

    print(dict.get('b'))

    print(request.META.get('CONTENT_LENGTH'))

    print(request.user)  #AnonymousUser匿名用户

    print(request.path)

    print(request.method)

    return HttpResponse('ojbk')

    response['itcast'] = 'python'

    return response


#5.response

def responsefunc(request):

    print('responsefunc')

    return HttpResponse('responsefunc', status=404)


def jsonFunc(request):


    print('jsonFunc')

    # dict = {
    #     'name':'zs',
    #     'age':123
    # }
    #
    # return JsonResponse(dict)

    # JsonResponse: 能自动把dict ===> json

    #json: 只有[], {}

    list = [{
        'name' : 'zs',
        'age' : 123
    }]

    return JsonResponse(list, safe=False)