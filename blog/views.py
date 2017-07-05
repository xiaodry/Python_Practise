# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    #request.POST
    #request.GET
    #return HttpResponse("hello world")
    return render(request, "index.html")
