from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

# Create your models here.

class Advertisement(models.Model):
    title=models.CharField("заголовок",max_length=128)
    text=models.TextField("текст")
    price=models.FloatField('цена')
    user=models.CharField("пользователь",max_length=126)
    create_at=models.DateTimeField("Дата создания",auto_now_add=True)
    update_at=models.DateTimeField("Дата обновления",auto_now=True)
    auction=models.BooleanField('торг',help_text='Возможен торг или нет',default=False)

    @admin.display(description='дата создания')
    def created_date(self):
        if self.create_at.date() == timezone.now().date():
            created_time=self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style= "color:green; font-weight=bold;">Сегодня в {}</span>',created_time
            )
        return self.create_at.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.update_at.date() == timezone.now().date():
            updated_time=self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style= "color:green; font-weight=bold;">Сегодня в {}</span>',updated_time
            )
        return self.update_at.strftime('%d.%m.%Y at %H:%M:%S')

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    class Meta:
        db_table = 'advertisements'

