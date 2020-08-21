import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Events(models.Model):
    EventCategory = models.TextChoices('EventCategory', 'CONFERENCE SEMINAR CONGRESS COURSE')
    EventType = models.TextChoices('EventType', 'VIRTUAL PRESENCIAL')
    event_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    event_name = models.CharField(max_length=200)
    event_category = models.CharField(choices=EventCategory.choices, max_length=15)
    event_place = models.CharField(max_length=200)
    event_address = models.CharField(max_length=200)
    event_initial_date = models.DateTimeField()
    event_final_date = models.DateTimeField()
    event_type = models.CharField(choices=EventType.choices, max_length=15)
    thumbnail = models.CharField(max_length=200)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Events, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
