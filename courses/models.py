from django.db import models


# Método para buscar cursos
class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )


# Create your models here.
class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Código')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    imagem = models.ImageField(upload_to='courses/imagens', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    objects = CourseManager()
