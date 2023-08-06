from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, visitor . You're at the projects index. <a href=\"/admin\">Visit Admin Site</a>")
