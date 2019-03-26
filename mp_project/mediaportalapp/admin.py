from django.contrib import admin

from mediaportalapp.models import Category, Article, Comments, UserAccount


admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comments)
admin.site.register(UserAccount)


# Register your models here.
