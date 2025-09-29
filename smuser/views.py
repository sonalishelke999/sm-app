from django.shortcuts import render
from .models import Smuser
# Create your views here.

def hello(request):
    if request.method == "POST":
        firstname= request.POST.get('firstname')
        image=request.FILES.get('image')
        u1 = Smuser.objects.create(firstname=firstname, image=image)
        return render (request,'b.html',{'smuser': u1})
        
    return render (request,'a.html')

def newhello(request):
    return render (request,'b.html')