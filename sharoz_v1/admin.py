from django.contrib import admin

# Register your models here.

from .models import Product, Photo, Color, Suggestion

admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Color)
admin.site.register(Suggestion)
