from django.contrib import admin

from .models import Event, Idea, IdeaUpvote


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "organizer",
        "start_date",
        "end_date",
        "is_approved",
    )


class IdeaAdmin(admin.ModelAdmin):
    pass

class IdeaUpvoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(IdeaUpvote, IdeaUpvoteAdmin)
