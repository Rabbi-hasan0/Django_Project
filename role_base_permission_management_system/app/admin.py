from django.contrib import admin
from .models import *
from django.utils.html import format_html


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(UserPermission)


# Register your models here.


# class PostAdmin(admin.ModelAdmin):
#     list_display=('title', 'category', 'image_preview')

#     def image_preview(self, obj):
#         if(obj.image):
#             return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
#         return "no image"
#     image_preview.short_description='Image Preview'
