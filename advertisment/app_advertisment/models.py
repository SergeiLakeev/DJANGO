from django.db import models


class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length= 12 )
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    created_at= models.DateTimeField('Дата и время создания', auto_now_add=True)
    updatet_at = models.DateTimeField('Дата и время изменения', auto_now=True)



