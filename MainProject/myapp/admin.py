from django.contrib import admin

# Register your models here.
from .import models

class BannersAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')
admin.site.register(models.Banners,BannersAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(models.Service,ServiceAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(models.Page,PageAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display = ('quest', 'ans')
admin.site.register(models.Faq,FaqAdmin)