from django.contrib import admin
from livebroadcast.models import Livebroadcast,Trip,Comment
class LivebroadcastAdmin(admin.ModelAdmin):
    list_display=('country','streamer','area')
    search_fields=('country','streamer')
class TripAdmin(admin.ModelAdmin):
    list_display=('country','comment','price')
    list_filter=('hotel',)
    fields=('price','livebroadcast')
    ordering=('-price',)

admin.site.register(Livebroadcast,LivebroadcastAdmin)
admin.site.register(Trip,TripAdmin)
admin.site.register(Comment)
# Register your models here.
