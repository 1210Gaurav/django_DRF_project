from django.contrib import admin
from .models import WatchList,StreamPlatform,Review
# Register your models here.


class WatchListAdmin(admin.ModelAdmin):
    list_display = ['id','title','storyline','active','created']
    
admin.site.register(WatchList, WatchListAdmin)

class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['id','name','about','website']
admin.site.register(StreamPlatform, StreamPlatformAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','rating','description','watchlist','active','created','updated']
admin.site.register(Review, ReviewAdmin)