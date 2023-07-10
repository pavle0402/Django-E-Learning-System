from django.utils import timezone
from .models import Announcement
from celery import shared_task

@shared_task
def delete_expired_announcements():
    current_time = timezone.now()
    expired_announcements = Announcement.objects.filter(expiry_date__lte=current_time)
    expired_announcements.delete()