from django.contrib import admin

from .models import Product,ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active','updated']
    date_hierarchy = 'timestamp'
    search_fields = ['title']
    list_editable = ['price','active']
    list_filter = ['price','active']
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
