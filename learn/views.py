# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import fileimg
import json
from django.http import JsonResponse
from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render
from django.template import RequestContext
from django.contrib import auth

STANDARD_HEADERS = ['REFER', 'HOST']
def index(request):
    return HttpResponse("欢迎自诩")



@requires_csrf_token

def home(request):
    # TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    TutorialList=fileimg.objects.all()
    # return HttpResponse(str(TutorialList))
    # TutorialList = models.person.object.all()
    #return render(request, 'home.html', {'TutorialList': TutorialList})
    return render_to_response('home.html', {'TutorialList': TutorialList})


def add(request):
    #Person.objects.create(name="WeizhongTu", age=24)

    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def  login(request):
    username = request.POST['username']
    password = request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            auth.login(request,user)
            context={'result':'login success!'}
    else:
        context={'result':'login failed!'}
    return render_to_response('home.html',context,context_instance=RequestContext(request))


def new(request):
    username = request.POST['name']
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}

    return JsonResponse({'d':username})

def new1(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    #return HttpResponse(json.dumps(response_data),content_type="application/json")
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}

    return JsonResponse(name_dict)
    #return HttpResponse('index.html',context_instance=RequestContext(request))
    context = {"js": "hello baby"}
    # return render_to_response('home.html',context,context_instance=RequestContext(request))
# Create your views here.
