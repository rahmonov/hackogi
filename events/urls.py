from django.urls import path

from events.views import EventDetailView

app_name = "events"
urlpatterns = [
    path("<int:event_id>/", EventDetailView.as_view(), name="event-detail"),
]
