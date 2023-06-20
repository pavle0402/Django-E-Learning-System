from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse
from django.conf import settings
import os
from django.contrib import auth
from datetime import datetime, date
from django.core.exceptions import ValidationError
from django.db.models import Avg, Count, Sum
from django.forms import inlineformset_factory
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm)
from .models import (User, Course, Announcement, UserProfile)
from .forms import (StudentSignupForm, CreateProfileForm)


class UserStatus(DetailView):
    model = User
    fields = ('is_teacher', 'is_learner')
    context_object_name = 'status'
    template_name = 'home.html'


#general views
def home_page(request):
    course1 = Course.objects.filter(id=2).first()
    course2 = Course.objects.filter(id=1).first()
    course3 = Course.objects.filter(id=8).first()

    context ={
        'course1': course1,
        'course2': course2,
        'course3': course3,
    }
    return render(request, 'home.html', context)

def about_page(request):
    return render(request,'about.html', {})

def services_page(request):
    return render(request, 'services.html', {})

def policy_page(request):
    return render(request, 'policy.html', {})

def contact_page(request):
    return render(request,'contact.html', {})

#account creating and logging in
def SignupStudentView(request):
    if request.method == "POST":
        form = StudentSignupForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully completed your registration.")
            return redirect('home')            
    else:
        form = StudentSignupForm()

    return render(request, "student_signup.html", {"form":form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f"Welcome back {username}. Nice to see you again.")
            return redirect('home')
            # if user.is_learner:
            #     return redirect('home')
            # if user.is_teacher:
            #     return redirect('about')
            # if user.is_superuser:
            #     return redirect('admin')
        else:
            messages.info(request, f"Incorrect login information. Try again.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')



class CourseListView(ListView):
    model = Course
    queryset = Course.objects.all()
    template_name = "course_list.html"
    context_object_name = "course"
    
class CourseDetailView(DetailView):     
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'


def InstructorsView(request):
    return render(request, 'instructors.html', {})


class AnnouncementView(ListView):
    model = Announcement
    template_name = "announcement.html"
    context_object_name = "announcements"
    


#staff and admin views

class CreateAnnouncementView(CreateView):
    model = Announcement
    template_name = "create_announcement.html"
    fields = "__all__"
    success_url = reverse_lazy('announcements')


class UpdateAnnouncementView(UpdateView):
    model = Announcement
    template_name = "edit_announcement.html"
    fields = "__all__"
    success_url = reverse_lazy('announcements')

class DeleteAnnouncementView(DeleteView):
    model = Announcement
    template_name = "delete_announcement.html"
    success_url = reverse_lazy('announcements')

#profile views

class ProfileCreateView(CreateView):
    model = UserProfile
    template_name = "create_profile.html"
    form_class = CreateProfileForm
    success_url = reverse_lazy('profile_page')


class EnrollCourse(View):
    def post(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        user_profile = UserProfile.objects.get(user=self.request.user)
        user_profile.courses.add(course)
        return reverse_lazy('home')
        #put profile_page for reverse_lazy when u make it

class ProfileDetailView(DetailView):
    model = UserProfile 
    context_object_name = "userprofile"
    template_name = "user_profile.html"



# class AddFeedbackView(View):
    
#     def post(self,request, course_id):
#         form = FeedbackForm(request.POST or None)
#         if form.is_valid():
#             course = Course.objects.filter(id=course_id)
#             feedback = CourseFeedback(
#                 course=course,
#                 name=request.user
#             )