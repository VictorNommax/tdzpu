from django.db import models

# Create your models here.
class Products(models.Model):
    exist = models.BooleanField('Наличие')
    name = models.CharField('Наименование',max_length=250)
    descsm = models.CharField('Краткое описание',max_length=250)
    desc = models.TextField('Описание')
    attr = models.TextField('Свойства',max_length=2000)
    photo = models.ImageField('Фотография',upload_to='static/images')
    photosm = models.ImageField('Миниатюра',upload_to='static/images/mini')
    info = models.TextField('Доп. информация',max_length=1000)

    en = models.CharField('Translit',max_length=250, default='_')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
