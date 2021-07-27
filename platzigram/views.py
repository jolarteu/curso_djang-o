from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import json



def hello_wolrd(request):
    now= datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('holaaa mundo, la hora es {now}'.format(now=str(now)))


def sort_numbers(request):
   ## import pdb; pdb.set_trace()
    numbers=(request.GET['numbers']).split(',')
    int_n=[int(i) for i in numbers]
    int_n=sorted(int_n)
    data={
        'status': 'ok',
        'numeros': int_n,
        'message': 'sorted numbers'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
 #   return HttpResponse("hiiiiiiiiiiiiiii")

def hi(request, name, age):
    if age<15:
        message=name+" no puedes entrarrr sad :("
    else:
        message="holaaaa "+name+ "bienvenido a Platzi"
    return HttpResponse(str(message))
