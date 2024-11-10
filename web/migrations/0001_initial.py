# Generated by Django 5.1 on 2024-11-09 17:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactForm",
            fields=[
                (
                    "contact_form_uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Contact_id",
                    ),
                ),
                (
                    "customer_email",
                    models.EmailField(max_length=254, verbose_name="Email_Cliente"),
                ),
                (
                    "customer_name",
                    models.CharField(max_length=64, verbose_name="Nombre_Cliente"),
                ),
                ("message", models.TextField(verbose_name="mensaje")),
            ],
            options={
                "verbose_name": "Formulario de contacto",
                "verbose_name_plural": "Formulario de contactos",
                "db_table": "ContactForm",
            },
        ),
        migrations.CreateModel(
            name="Flan",
            fields=[
                (
                    "flan_uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Flan_id",
                    ),
                ),
                ("name", models.CharField(max_length=64, verbose_name="Nombre")),
                ("description", models.TextField(verbose_name="Descripcion")),
                ("image_url", models.URLField(verbose_name="Imagen_url")),
                ("slug", models.SlugField(verbose_name="Slug")),
                ("is_private", models.BooleanField(verbose_name="Privado")),
            ],
            options={
                "verbose_name": "Flan",
                "verbose_name_plural": "Flanes",
                "db_table": "Flanes",
            },
        ),
    ]