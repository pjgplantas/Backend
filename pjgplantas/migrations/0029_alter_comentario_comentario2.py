# Generated by Django 4.0.6 on 2022-09-25 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pjgplantas', '0028_remove_midia_planta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]