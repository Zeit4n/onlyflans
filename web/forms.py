from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactForm

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name','customer_email','message']

        widgets = {
            'customer_name':forms.TextInput(attrs={'class':'form-control mb-3','type':'text'}),
            'customer_email':forms.TextInput(attrs={'class':'form-control mb-3','type':'text'}),
            'message': forms.Textarea(attrs={'class':'form-control mb-3','type':'text'})
        }
        labels = {
            'customer_name':'Nombre',
            'customer_email':'Email',
            'message':'Mensaje'
        }

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','password']

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control mb-3','type':'text'}),
            'email': forms.EmailInput(attrs={'class':'form-control mb-3','type':'text'}),
            'password':forms.PasswordInput(attrs={'class':'form-control mb-3','type':'password'}),
        }

        labels = {
            'username':'Nombre de usuario',
            'email': 'Correo electrónico',
            'password': 'Contraseña',
        }

class UserLoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',  'password']

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control mb-3','type':'text'}),
            'password':forms.PasswordInput(attrs={'class':'form-control mb-3','type':'password'}),
        }

        labels = {
            'username':'Nombre de usuario',
            'password': 'Contraseña',
        }