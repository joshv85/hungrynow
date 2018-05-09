"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *

def mdex(request):
    return render(request, 'app/mdex.html')

def rest_display(request):
    return render(request, 'app/rest_display.html')

def rtemplate(request):
    rteinv = rtemptime.objects.order_by('-id')[0:1]
    return render(request, 'app/rtemplate.html', {'rtemplate' : rteinv},)

def rtimeenter(request):
        if request.method == "GET":
            form = RenterForm()
            return render(request, 'app/rtimeenter.html', { 'form':form }, )

        elif request.method == "POST" :
            form = RenterForm(request.POST)
            form.save()
            return HttpResponseRedirect('/rtimeenter')


