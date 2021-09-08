from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fun1(request):
    return render(request,"add.html",{"name":"surbhi"})


def add(request):
     val1 = int(request.GET['n1'])
     val2 = int(request.GET['n2'])

     res = val1+val2
     return render(request,"result.html",{'result':res})
