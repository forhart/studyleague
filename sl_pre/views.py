# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from sl_pre.models import Stream

def streams_list(request):
    streams = Stream.objects.all()
    return render_to_response('streams.html',{'streams_list': streams })
