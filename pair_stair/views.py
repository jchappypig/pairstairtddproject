from django.shortcuts import render_to_response
from django.template.context import RequestContext

def add_programmer_index(request):
    return render_to_response("add_programmer.html", RequestContext(request))