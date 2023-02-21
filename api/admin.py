from django.contrib import admin
from .models import UsersModel, CategoryModel, ProductModel
# Register your models here.

admin.site.register(UsersModel)
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
