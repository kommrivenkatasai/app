from django.shortcuts import render, redirect
from .models import Students,Kathabooks
from django.contrib import sessions
from django.core.mail import send_mail
from django.conf import settings
from random import randint
def Login(request):
    if request.method=='POST':
            phnumber=request.POST['phnumber']
            request.session['phnumber']=phnumber
            password=request.POST['password']
            student = Students.objects.filter(phnumber=phnumber).first()
            if student and student.password == password:
                      return redirect('main')
            else:
                return render(request, 'login.html', {'show_popup': True})
    return render(request,'login.html')

def Signup(request):
    if request.method == 'POST':
        phnumber = request.POST['phnumber']
        email = request.POST['email']
        existing_student = Students.objects.filter(phnumber=phnumber,email=email).first()
        if existing_student:
            return render(request, 'signup.html', {'show_popup': True})
        name = request.POST['name']
        
        altnumber = request.POST['altphnumber']
        college = request.POST['college']
        password = request.POST['password']
        data = Students(name=name, email=email, phnumber=phnumber, altphnumber=altnumber, college=college, password=password)
        data.save()
    return render(request, 'signup.html')

def Views(request):
    students=Students.objects.all().values()
    context={
        'students':students,
    }
    return render(request,'view.html',context)


def Forgot(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        student = Students.objects.filter(email=email).first()
        if student:
            global otp
            otp=randint(1000,9999)
            subject = 'Password Reset Request'
            message = (
                f'Dear User,\n\n'
                f'You have requested to reset your password. Please use the following OTP to proceed:\n\n'
                f'OTP: {otp}\n\n'
                f'If you did not request this, please ignore this email.\n\n'
                f'Thank you,\nSri Dugra Curry Point Team'
            )
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('otp',email=email)
        else:
            return render(request, 'forgot.html', {'show_popup': True})

    return render(request, 'forgot.html')

def Otp(request, email):
    if request.method == 'POST':
        uotp = request.POST.get('otp')
        print(otp,uotp)
        if int(otp)==int(uotp):
            return redirect('cnp', email=email)
        else:
            return render(request, 'otp.html', {'show_popup': True})
    
    return render(request, 'otp.html', {'email': email})

def Cnp(request,email): 
    if request.method=="POST":
        password = request.POST['password']
        x=Students.objects.all()
        for i in x:
            if i.email==email:
                i.password=password
                i.save()
    return render(request,'cnp.html')
def Main(request):
    phnumber=request.session['phnumber']
    student_deatiles=Students.objects.all().filter(phnumber=phnumber).first()
    context={
        "student":student_deatiles,
    }
    return render(request,'main.html',context)
def Add(request):
    if request.method=="POST":
        datatime=request.POST["datetime"].split("T")
        timeofday=request.POST["timeofday"]
        ammount=request.POST["amount"]
        phnumber=request.session['phnumber']
        data=Kathabooks(phnumber=phnumber,date=datatime[0],timeofday=timeofday,amount=ammount)
        data.save()
        return redirect('due')
    return render(request,'add.html')
def Due(request):
    phnumber=request.session['phnumber']
    student_deatiles=Students.objects.all().filter(phnumber=phnumber).first()
    student_katha=Kathabooks.objects.all()
    context={
        "student":student_deatiles,
        "phnumber":phnumber,
        "khatha":student_katha,
    }
    return render(request,'duehistory.html',context)