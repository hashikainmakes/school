from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Programming,Course


# Create your views here.

def demo(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        pwd = request.POST['Pass']
        cpwd = request.POST['con_pass']
        if pwd == cpwd:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "Enter Username ")
                return redirect('schoolapp:register')
            else:
                user = User.objects.create_user(username=user_name, password=pwd)
                user.save()
                return redirect('schoolapp:login')
        else:
            messages.info(request, 'Password not match')
            return redirect('schoolapp:register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['pass']
        Login = auth.authenticate(username=username, password=password)
        if Login is not None:
            auth.login(request, Login)
            return redirect('schoolapp:accept')
        else:
            messages.info(request, 'Invalid User')
            return redirect('login')
    return render(request, 'login.html')
def accept(request):
    return render(request, "loginaccept.html")
def index(request):
    program=Programming.objects.all()
    d={'program':program}
    return render(request,"home.html",d)
def load_courses(request):
    programming_id=request.GET.get('programming')
    courses=Course.objects.filter(programming_id=programming_id).order_by('name')
    return render(request,"form.html",{'courses':courses})

def submit(request):
    return render(request, 'order_sucess.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

