# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from sl_pre.models import Stream,Semester,Subject,Chapter

def stream_list(request):
    streams = Stream.objects.all()
    return render_to_response('streams.html',{'streams_list': streams })


def plan_list(request):
    return HttpResponse("<h1>Plan and Subscription</h1>")


def semester_list(request,stream_slug):
    stream = get_object_or_404(Stream,slug=stream_slug)
    return HttpResponse(stream.title + stream.slug)
    
    
