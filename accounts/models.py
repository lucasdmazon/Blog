from django.contrib.auth.models import User
from django.db import models


class Documento(models.Model):
    arquivo = models.FileField(upload_to='pdf/')
