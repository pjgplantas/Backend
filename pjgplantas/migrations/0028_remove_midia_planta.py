# Generated by Django 4.0.6 on 2022-09-25 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pjgplantas', '0027_delete_tipousuario_delete_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midia',
            name='planta',
        ),
    ]
