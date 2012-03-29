# Create your views here.
from django.http import HttpResponse

def streams_list(request):
    return HttpResponse("Hello WOrld")
