# Generated by Django 4.0.6 on 2023-05-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_publicado_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.BooleanField(default=False, verbose_name='like'),
        ),
    ]
