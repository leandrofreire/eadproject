from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Código')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    imagem = models.ImageField(upload_to='courses/imagens', verbose_name='Imagem')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
