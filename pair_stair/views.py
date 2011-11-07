from django.shortcuts import render_to_response
from django.template.context import RequestContext
from pair_stair.models import Programmer

def add_programmer_index(request):
    if request.method == 'POST':
        programmer_name = request.POST['programmer_name_tb']
        add_programmer(programmer_name)
    return render_to_response("add_programmer.html", RequestContext(request))

def add_programmer(programmer_name):
    programmer = Programmer(name = programmer_name)
    programmer.save()

def pair_stair_index(request):
    return render_to_response("pairStair.html", RequestContext(request))