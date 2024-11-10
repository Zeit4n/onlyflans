from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label = 'Correo')
    customer_name = forms.CharField(max_length = 64, label = 'Nombre')
    message = forms.CharField(label = 'Mensaje')

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