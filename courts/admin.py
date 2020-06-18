from django.contrib import admin
from .models import Court, MapStyle, MapAPIKey, Signup
from django.contrib.admin.models import LogEntry

# Support logging admin actions
class LogEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('content_type',
        'user',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    )

    def has_delete_permission(self, request, obj=None):
        return False


# Customize admin page for MapStyle to show different data in columns
class MapStyleAdmin(admin.ModelAdmin):
    list_display = ('description', 'map_style', 'active')
    search_fields = ['description']

# Customize admin page for MapStyle to show different data in columns
class CourtAdmin(admin.ModelAdmin):
    list_display = ('id','name','road','city','state')
    search_fields = [ 'name', 'road','city', 'state', 'id']
    list_filter = ['likes', 'dislikes','state','country']

class MapAPIKeyAdmin(admin.ModelAdmin):
    list_display = ('api_key', 'active')
    search_fields = ['api_key']

    def has_delete_permission(self, request, obj=None):
        return False

class SignupAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ['email']

# Register your models here.
admin.site.register(Court, CourtAdmin)
admin.site.register(MapAPIKey, MapAPIKeyAdmin)
admin.site.register(MapStyle, MapStyleAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(Signup, SignupAdmin)