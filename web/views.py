from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Flan, ContactForm
from .forms import ContactFormForm, UserLoginForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    context ={
        'flanes':Flan.objects.all().filter(is_private = False),
    }    
    return render(request,'index.html',context)
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
            return HttpResponseRedirect('exito')
    
    else:
        form = ContactFormForm()
    context = {
        'form':form
    }
    return render(request, 'contact.html', context)

def success(request):
    return render(request,'success.html')