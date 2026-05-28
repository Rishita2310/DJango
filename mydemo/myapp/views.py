from django.shortcuts import render,HttpResponse

# Create your views here.

def hello1(request):
    return HttpResponse("hello")


def bye(request):
    return HttpResponse("bye")

def sayo(request):
    return HttpResponse("Sayonara")

def html1(request):
    return render(request,"1.html")


def html2(request):
    return render(request,"2.html")


def html3(request):
    return render(request,"3.html")
