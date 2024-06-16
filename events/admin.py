from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "organizer",
        "start_date",
        "end_date",
        "is_approved",
    )


admin.site.register(Event, EventAdmin)
