from django.shortcuts import render_to_response
from django.template.context import RequestContext
from pair_stair.models import Programmer, Pair

def add_programmer_index(request):
    if request.method == 'POST':
        programmer_name = request.POST['programmer_name_tb']
        add_programmer(programmer_name)
    return render_to_response("add_programmer.html", RequestContext(request))


def add_programmer(programmer_name):
    programmer = Programmer(name=programmer_name)
    programmer.save()
    add_pairs()

def add_pairs():
    number_of_programmers = Programmer.objects.count()
    for index_of_programmer in range(number_of_programmers - 1):
        if not number_of_programmers == 1:
            pair = Pair(programmer1=Programmer.objects.all()[number_of_programmers - 1],
                        programmer2=Programmer.objects.all()[index_of_programmer], count=0)
            pair.save()

def pair_stair_index(request):

    programmers = Programmer.objects.all()
    pairs = Pair.objects.all()
    return render_to_response("pairStair.html", {'programmers':programmers, 'pairs':pairs})

def remove_programmers_index(request):
    Programmer.objects.all().delete()
    return render_to_response("remove_all_programmers.html",RequestContext(request))


def mark_pair(request, programmer1_id, programmer2_id):
    pair = Pair.objects.get(programmer1=Programmer.objects.get(id=programmer1_id), programmer2=Programmer.objects.get(id=programmer2_id))
    pair.count += 1
    pair.save()
    return pair_stair_index(request)