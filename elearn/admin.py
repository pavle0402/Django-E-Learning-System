from django.contrib import admin
from .models import User, Course, Announcement, UserProfile, Feedback

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Announcement)
admin.site.register(UserProfile)
admin.site.register(Feedback)



