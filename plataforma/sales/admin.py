from django.contrib import admin

from .models import Sale, SaleDetail

class SaleAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    ordering = ('created',)
    search_fields = ('company', 'saleManager', 'buyerName')
    list_filter = ('company',)

class SaleDetailAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    ordering = ('created',)
    search_fields = ('product', 'amount')

admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleDetail, SaleDetailAdmin)