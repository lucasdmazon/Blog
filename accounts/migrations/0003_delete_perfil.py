# Generated by Django 4.0.6 on 2023-05-15 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_perfil_nome_completo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
