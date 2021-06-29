from django.shortcuts import render
from user.models import user
from django.core.mail import send_mail
from django.conf import settings
# from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def index(request):
       
    if request.method=="POST":
        name=request.POST.get('name',True)
        phon=request.POST['phon']
        dateof=request.POST['date']
        email=request.POST['email']
        ins=user(name=name,email=email,dob=dateof,telephone=phon)
        ins.save() 
        send_mail(
        'test',
        'this msg is for testing purpose.this is auto genrated mail plz dont reply to this msg ',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,)   
        return HttpResponse("submitted")
    else:
        return render(request,'index.html')
    return render(request,'index.html')
def display(request):
    # if request.methode=="POST":
        ins=user.objects.all()
        return render(request, 'display.html',{'re':ins})
