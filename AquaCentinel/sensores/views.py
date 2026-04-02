from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "index.html")
    return HttpResponse("Hola desde sensores")