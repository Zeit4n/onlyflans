from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Flan, ContactForm
from .forms import ContactFormForm, UserLoginForm, UserRegisterForm
from django.http import HttpResponseRedirect
import json
# Create your views here.
def index(request):
    if request.method == 'GET':
        context ={
            'flanes':Flan.objects.all().filter(is_private = False),
        }    
        return render(request,'index.html',context)
    elif request.method == 'POST':
        data = json.loads(request.body)
        user_rate = data.get('user_rate')
        flan_id = data.get('flan_id')
        flan_edit = Flan.objects.get(flan_uuid=flan_id)
        flan_edit.rate = user_rate
        flan_edit.save()
        context = {
            'user' : request.user,
            'flanes' : Flan.objects.all().filter(is_private = False),
            }
        return render(request,'welcome.html',context)

def register(request):
    if request.method == 'GET':
        context = {
            'form':UserRegisterForm,
            'title':'Registro'
        }
        return render(request,'register.html',context)
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST['password'])
            user.save()
            return redirect('log_in')
        else:
            return render(request,'register.html',{'form':form,'title':'Registro'})
    
def log_in(request):
    if request.method == 'GET':
        context = {
            'form':UserLoginForm,
            'title':'Inicio de sesión'
        }
        return render(request,'log_in.html',context)
    elif request.method == 'POST':
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            context = {
                'form':UserLoginForm,
                'title':'Log In',
                'error': f'El usuario {request.POST["username"]} y/o contraseña {request.POST["password"]} son incorrectos'
            }
            return render(request,'log_in.html',context)
        else:
            login(request,user=user)
            return redirect('welcome')
        
def log_out(request):
    logout(request)
    return redirect('index')

def about(request):
    return render(request,'about.html')

@login_required
def welcome(request):
    if request.method == 'GET':
        context = {
            'user' : request.user,
            'flanes' : Flan.objects.all().filter(is_private = True),
            }
        return render(request,'welcome.html',context)
    elif request.method == 'POST':
        data = json.loads(request.body)
        user_rate = data.get('user_rate')
        flan_id = data.get('flan_id')
        flan_edit = Flan.objects.get(flan_uuid=flan_id)
        flan_edit.rate = user_rate
        flan_edit.save()
        context = {
            'user' : request.user,
            'flanes' : Flan.objects.all().filter(is_private = True),
            }
        return render(request,'welcome.html',context)

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            contact_form.save()
            return redirect('index')
    
    else:
        form = ContactFormForm()
    context = {
        'form':form
    }
    return render(request, 'contact.html', context)

def success(request):
    return render(request,'success.html')