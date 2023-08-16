from django.db import models

# Create your models here.

class Advertisement(models.Model):
    title=models.CharField("заголовок",max_length=128)
    text=models.TextField("текст")
    price=models.FloatField('цена')
    user=models.CharField("пользователь",max_length=126)
    date=models.DateField("дата",auto_now_add=True)
    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    class Meta:
        db_table = 'advertisements'