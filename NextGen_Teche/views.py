# from django.http import HttpResponse
from django.shortcuts import render 
from contact.models import Contact
from product.models import Product
from service.models import Service
from recruitment.models import Recruitment
from internship.models import Internship
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request,"index.html")

def product(request):
    products = Product.objects.all()
    data={
        'products':products
    }
    return render (request,"product.html",data)

def service(request):
    services = Service.objects.all()
    data={
        'services':services
    }
    return render(request,"service.html",data)

def internship(request):
    internships = Internship.objects.all()
    data={
        'internships':internships
    }
    return render(request,"internship.html",data)

def reform(request):
    if request.method == "POST" and request.FILES['resume']:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        position = request.POST.get('position')
        passout = request.POST.get('passout')
        experience = request.POST.get('experience')
        summary = request.POST.get('summary')
        resume = request.FILES['resume']
        # fs = FileSystemStorage()
        # filename = fs.save(resume.name, resume)
        # file_url = fs.url(filename)
        reform = Recruitment(name=name,email=email,phone=phone,address=address,gender=gender,position=position,passout=passout,experience=experience,summary=summary,resume=resume)
        reform.save()
    return render(request,"form.html")

def form(request):
    return render(request,"form.html")

def saveform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        con=Contact(name=name,email=email,phone=phone,message=message)
        con.save()
    return render(request,"contact.html")

def contact(request):
    return render(request,"contact.html")