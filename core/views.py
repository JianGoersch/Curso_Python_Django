from django.shortcuts import render, HttpResponse

# Create your views here.
def curso(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} </h1>'.format(nome, idade))