from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Event(BaseModel):
    organizer = models.ForeignKey(
        "accounts.CustomUser",
        on_delete=models.CASCADE,
        related_name="events",
        related_query_name="event",
    )

    title = models.CharField(_("title"), max_length=255)
    overview = models.TextField(_("overview"))

    start_date = models.DateTimeField(_("start date"))
    end_date = models.DateTimeField(_("end date"))

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Idea(BaseModel):
    event = models.ForeignKey(
        Event, related_name="ideas", related_query_name="idea", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        "accounts.CustomUser",
        related_name="ideas",
        related_query_name="idea",
        on_delete=models.CASCADE,
    )
    title = models.CharField(_("title"), max_length=255)
    overview = models.TextField(_("overview"))

    def __str__(self):
        return self.title


class IdeaUpvote(BaseModel):
    idea = models.ForeignKey(
        Idea,
        related_name="upvotes",
        related_query_name="upvote",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "accounts.CustomUser",
        related_name="upvotes",
        related_query_name="upvote",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("idea", "user",)

    def __str__(self):
        return f"{self.user} likes {self.idea.title}"
