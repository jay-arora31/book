from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    book_name = models.CharField( verbose_name='Book Name', null=True, blank=True,max_length = 200)
    author = models.CharField(verbose_name='Author', null=True, blank=True,max_length = 200)
    genre  = models.CharField(verbose_name='Genre', null=True, blank=True,max_length = 200)
    language = models.CharField(verbose_name='Language', null=True, blank=True,max_length = 200)
    def __str__(self):
        return self.book_name