import sys
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from test1.models import *
from test1.forms import *

# Create your views here.

def cover(request):
    if not request.user.is_authenticated:
        return render(request,'cover.html')
    else:
        return redirect('home')
        

def loginview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request,'Invalid Credentials')
                return redirect('login')
        return render(request,'login.html')
    else:
        return redirect('home')


def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'logout.html')
    else:
        return redirect('lr')


def registerview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username=request.POST['username']
            email=request.POST['email']
            password=make_password(request.POST['password'])
            myuser = User.objects.create_user(username,email,password)
            myuser.save()
            return redirect('login')

        return render(request,'register.html')
        
    else:
        return redirect('home')


@login_required(login_url='lr')
def home(request):
    return render(request,'home.html')


@login_required(login_url='lr')
def interveiw(request):
    return render(request,'interview.html')


@login_required(login_url='lr')
def exam(request):
    return render(request,'exam.html')


@login_required(login_url='lr')
def greetings(request):
    res = render(request,'h.html')
    return res
@login_required(login_url='lr')
def runcode(request):
    if request.method == 'POST':
        exam_models = exam_model.objects.all()
        context = {'context':context}
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        return render(request,'h.html',{"code":code_part,"input":y,"output":output},context,exam_models)
    return render(request,'h.html')


@login_required(login_url='lr')
def codingsection_completed(request):
    return render(request,'codingsection_completed.html')

@login_required(login_url='lr')
def score(request):
    return render(request,'score.html')


@login_required(login_url='lr')
def about(request):
    return render(request,'about.html')


@login_required(login_url='lr')
def contactview(request):
    return render(request,'contact.html')


def lr(request):
    if not request.user.is_authenticated:
        return render(request,'lr.html')
    else:
        return redirect('home')

def password_reset(request):
    if not request.user.is_authenticated:
        return render(request,'password_reset.html')
    else:
        return redirect('home')


def main_view(request):
    context = {}
    return render(request,'main.html',context=context)