from django.contrib import admin
from . models import Image
from django.utils.html import format_html
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display =('name','description','available','image_tag','image','updated_date')
    list_filter = ('available','created_date','updated_date')
    search_fields = ('name','description')
    def image_tag(self,obj):
        return format_html('<a href="{0}"><img src="{0}" style="width: 45px; height:45px;" /></a>'.format(obj.image.url))



