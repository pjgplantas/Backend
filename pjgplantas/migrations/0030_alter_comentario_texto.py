# Generated by Django 4.0.6 on 2022-09-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pjgplantas', '0029_alter_comentario_comentario2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.TextField(),
        ),
    ]