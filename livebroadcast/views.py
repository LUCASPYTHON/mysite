# -*- coding: utf-8 -*-
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,render
from livebroadcast.models import  Livebroadcast,Trip,Comment
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from livebroadcast.forms import CommentForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
#def travel(request):
#    if 'id' in request.GET and request.GET['id'] !='':
#        livebroadcast=Livebroadcast.objects.get(id=request.GET['id'])
#        return render_to_response('travel.html', locals())
#    else:
#        return HttpResponseRedirect("/livebroadcasts_list/")


def travel(request,id):
    if 'id' :
        livebroadcast=Livebroadcast.objects.get(id=id)
        return render_to_response('travel.html', locals())
    else:
        return HttpResponseRedirect("/livebroadcasts_list/")

@login_required
def list_livebroadcasts(request):
    path = request.path
    livebroadcasts = Livebroadcast.objects.all()
    print (request.user.user_permissions.all())
    request.session['livebroadcasts']=livebroadcasts
    return render_to_response('livebroadcasts_list.html',RequestContext (request,locals()))
@csrf_exempt
def comment(request,id):
    if id:
        l = Livebroadcast.objects.get(id=id)
    else:
        return HttpResponseRedirect("/livebroadcasts_list/")
    if request.POST:
        f=CommentForm(request.POST)
        if f.is_valid():
            user = f.cleaned_data['user']
            content = f.cleaned_data['content']
            email = f.cleaned_data['email']
            date_time = datetime.datetime.now()     # 擷取現在時間
            c=Comment.objects.create( user=user,email=email, content=content, date_time=date_time, livebroadcast=l)
            f= CommentForm(initial={'content':'我沒意見'})
    else:
        f=CommentForm(initial={'content':'我沒意見'})
    return render(request,'comments.html',locals())
    #return render_to_response('comments.html',{'form':form}, RequestContext(request) )
    #return render_to_response('comments.html', RequestContext(request, locals()))
def login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/index/')

    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)

    if user is not None and user.is_active:
        auth.login(request,user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html',locals())
def index(request):
    return render_to_response('index.html',locals())
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def user_can_comment(user):
    return user.is_authenticated and user.has_perm('livebroadcast.can_comment')
@user_passes_test(user_can_comment, login_url='/accounts/login/')
def comment(request,id):
    if request.user.is_authenticated and request.user.has_perm('livebroadcast.can_comment'):
        ...
    else:
        return HttpResponseRedirect("/livebroadcasts_list/")
