from django.shortcuts import render

def seller_master(request):
    return render(request,'frame/master.html')


def seller_home(request):
    return render(request,'frame/home.html')


def seller_about(request):
    return render(request,'frame/about.html')

def seller_contact(request):
    return render(request,'frame/contact.html')

# Create your views here.
