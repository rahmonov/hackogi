from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

from events.models import Event


class EventDetailView(View):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse("Event does not exist")

        return render(request, "events/event_detail.html", context={"event": event})
