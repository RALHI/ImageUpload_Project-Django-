from django.contrib import admin
from .models import image

# Register your models here.

class imageAdmin(admin.ModelAdmin):
  list_display = ("image_name","image","date")

admin.site.register(image,imageAdmin)
