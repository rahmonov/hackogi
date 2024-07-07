from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Exists, OuterRef
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from events.forms import CreateIdeaForm
from events.models import Event, Idea, IdeaUpvote


class EventDetailView(View):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse("Event does not exist")

        ideas = event.ideas.annotate(
            is_liked=Exists(
                IdeaUpvote.objects.filter(user=request.user, idea=OuterRef("pk"))
            )
        )
        context = {"event": event, "idea_form": CreateIdeaForm(), "ideas": ideas}

        return render(request, "events/event_detail.html", context=context)


class CreateEventIdeaView(LoginRequiredMixin, View):
    def post(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse("Event does not exist")

        form = CreateIdeaForm(request.POST)

        if form.is_valid():
            Idea.objects.create(
                owner=request.user,
                event=event,
                title=form.cleaned_data["title"],
                overview=form.cleaned_data["overview"],
            )

        return redirect("events:event-detail", event_id=event.id)


class UpvoteIdeaView(LoginRequiredMixin, View):
    def post(self, request, event_id, idea_id):
        try:
            idea = Idea.objects.get(id=idea_id, event__id=event_id)
        except Idea.DoesNotExist:
            return HttpResponse("Idea does not exist")

        IdeaUpvote.objects.create(idea=idea, user=request.user)

        return redirect("events:event-detail", event_id=event_id)
