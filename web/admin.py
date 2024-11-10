from django.contrib import admin
from .models import Flan, ContactForm
from django.contrib.auth.models import User
# Register your models here.

class FlanAdmin(admin.ModelAdmin):
    list_display = ('Flan_id', 'Nombre', 'Descripcion','Imagen_url','Slug','Privado','Valoración')

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('Contact_id', 'Nombre_Cliente', 'Email_Cliente','mensaje')

admin.site.register(Flan)
admin.site.register(ContactForm)
