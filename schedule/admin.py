from django.contrib import admin
from .models import Event, Dates, Configuration


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "start_time", "end_time", "owner")
    list_filter = ("title", "description", "start_time", "end_time", "owner")
    search_fields = ("title", "description", "owner")


class DatesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "start_time", "end_time", "requester", "agent")
    list_filter = ("title", "description", "start_time", "end_time", "requester", "agent")
    search_fields = ("title", "description", "requester", "agent")


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ("id", "parameter", "value")
    list_filter = ("parameter", "value")
    search_fields = ("parameter", "value")


admin.site.register(Event, EventAdmin)
admin.site.register(Dates, DatesAdmin)
admin.site.register(Configuration, ConfigurationAdmin)

