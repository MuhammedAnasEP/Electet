from django.contrib import admin
from home.models import Categorys, Products

# Register your models here.
class CategorysAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Categorys, CategorysAdmin)

class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)}

admin.site.register(Products, ProductsAdmin)