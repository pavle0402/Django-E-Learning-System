from django.db import models 
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils.html import escape, mark_safe




class User(AbstractUser):
    is_learner = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False, null=True)
    is_admin = models.BooleanField(default=False, null=True)


class Course(models.Model):
    name = models.CharField(max_length=155, blank=False)
    description = models.TextField()
    color = models.CharField(default='#00bbff', max_length=7)
    badge = models.ImageField(upload_to="images")
    price = models.CharField(default='50.99$', max_length=10)
    instructor = models.CharField(max_length=155, null=True)

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)

    def __str__(self):
        return f"{self.name} - {self.instructor}"



class Announcement(models.Model):
    title = models.CharField(max_length=155, blank=False)
    added_on = models.DateTimeField(auto_now_add=True)
    text = RichTextField()
    file = models.FileField(upload_to="files", blank=True)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="images")
    bio = models.TextField()
    birth_date = models.CharField(max_length=11)