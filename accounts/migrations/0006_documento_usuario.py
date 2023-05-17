# Generated by Django 4.0.6 on 2023-05-17 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_rename_documentos_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]