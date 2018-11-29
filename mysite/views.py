# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import  UserCreationForm
def here(request):
    return HttpResponse('Travel,Here I come 我來了')
def math(request,a,b):
    a=int(a)
    b=int(b)
    s=a+b
    d=a-b
    p=a*b
    q=a/b
    t= get_template('math.html')
    c =template.Contest({'s':s,'d':d,'p':p,'q':q})
    return HttpResponse(t.render(c))
def travel(request):
    trip1 ={'country':'日本','price':15000,'comment':'文化悠久','hotel':False}

    trip2 ={'country':'台灣','price':10000,'comment':'小吃很多','hotel':False}
    trips=[trip1,trip2]
    return render_to_response('travel.html', locals())
def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())
def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login')
    else:
        form = UserCreationForm()
    return render_to_response('register.html',locals())