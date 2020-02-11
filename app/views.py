from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
# Create your views here.


def IndexPage(request):
    return render(request,"app/insert.html")



def ShowPage(request):
    all_user = Emp.objects.all()
    return render(request,"app/show.html",{'all_user':all_user})


def insertData(request):
    name = request.POST['fname']
    address = request.POST['address']
    city = request.POST['city']
    phone = request.POST['phone']

    newuser = Emp.objects.create(name=name,address=address,city=city,phone=phone)
    return HttpResponseRedirect(reverse("show"))

def EditPage(request,pk):
    euser = Emp.objects.get(pk=pk)
    return render(request,"app/edit.html",{'euser':euser})


def updateUser(request,pk):
    user = Emp.objects.get(pk=pk)
    user.name = request.POST['fname']
    user.address = request.POST['address']
    user.city = request.POST['city']
    user.phone = request.POST['phone']
    user.save()
    return HttpResponseRedirect(reverse("show"))

def DeleteUser(request,pk):
    deluser = Emp.objects.get(pk=pk)
    deluser.delete()
    return HttpResponseRedirect(reverse("show"))