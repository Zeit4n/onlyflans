import uuid
from django.db import models

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key = True, verbose_name = 'Flan_id')
    name = models.CharField(max_length = 64, verbose_name = 'Nombre')
    description = models.TextField(verbose_name = 'Descripcion')
    image_url = models.URLField(verbose_name = 'Imagen_url')
    slug = models.SlugField(verbose_name = 'Slug')
    is_private = models.BooleanField(verbose_name = 'Privado')
    rate = models.IntegerField(default = None, null = True, verbose_name = 'Valoración')

    class Meta:
        db_table = 'Flanes'
        verbose_name = "Flan"
        verbose_name_plural = "Flanes"

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key = True, verbose_name = 'Contact_id')
    customer_email = models.EmailField(verbose_name = 'Email_Cliente')
    customer_name = models.CharField(max_length = 64, verbose_name = 'Nombre_Cliente')
    message = models.TextField(verbose_name = 'mensaje')

    class Meta:
        db_table = 'ContactForm'
        verbose_name = "Formulario de contacto"
        verbose_name_plural = "Formulario de contactos"

"""
class Usuario(AbstractUser):
    confirm_password = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
"""
    