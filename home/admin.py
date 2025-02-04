from django.contrib import admin
from .models import HomeContent, HotelInfo

class HomeContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    ordering = ('title',)

class HotelInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'email')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(HomeContent, HomeContentAdmin)
admin.site.register(HotelInfo, HotelInfoAdmin)
