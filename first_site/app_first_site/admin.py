from django.contrib import admin
from .models import Advertisement
# Register your models here.

from django.db.models.query import QuerySet

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','text','price','user','create_at','update_at','auction','created_date','updated_date']
    list_filter = ['auction','create_at']
    actions = ['make_auction_as_false','make_auction_as_true']
    fieldsets = (
        ('Общее',{'fields':('title','text'),}),
        ('Финансы',{'fields':('price','auction'),'classes':['collapse']}),
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self,request,queryset:QuerySet):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self,request,queryset:QuerySet):
        queryset.update(auction=True)



admin.site.register(Advertisement,AdvertisementAdmin)