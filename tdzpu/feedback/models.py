from django.db import models

# Create your models here.
class Comments(models.Model):
    userid = models.IntegerField('ID Автора')
    user = models.CharField('Пользователь',max_length=250)
    text = models.TextField('Текст отзыва',max_length=1000)
    date = models.DateTimeField('Время', auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
