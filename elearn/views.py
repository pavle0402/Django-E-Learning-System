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
from django.http import HttpResponse
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm)
from .models import (User, Course, Announcement, UserProfile, Feedback)
from .forms import (StudentSignupForm, CreateProfileForm, FeedbackForm)
from django.http import JsonResponse
from django.contrib import messages



class UserStatus(DetailView):
    model = User
    fields = ('is_teacher', 'is_learner')
    context_object_name = 'status'
    template_name = 'home.html'


#general views
def navbar_view(request):
    userprofile = UserProfile.objects.all()
    context = {
        'userprofile': userprofile
    }
    return render(request, 'navbar.html', context)

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


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedbacks'] = Feedback.objects.filter(course=self.object)
        return context
    
class EnrollCourseView(View):
    def get(self, request, *args, **kwargs):
        return reverse_lazy('course_detail', pk=self.kwargs['course_id'])
    
    def post(self ,request, *args, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs['course_id'])
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.enrolled_courses.add(course)
        return messages.success(request, "You have successfully bought this course.")
    
    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk':self.kwargs['pk']})
    

def InstructorsView(request):
    return render(request, 'instructors.html', {})


class AnnouncementView(ListView):
    model = Announcement
    template_name = "announcement.html"
    context_object_name = "announcements"
    ordering = ['-added_on']


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
    success_url = reverse_lazy('home')    
    # def get_success_url(self):
    #     return reverse_lazy('profile_page', kwargs={'pk':self.kwargs['pk']})


class ProfileDetailView(DetailView):
    model = UserProfile 
    context_object_name = "userprofile"
    template_name = "user_profile.html"

#feedback
class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = 'add_feedback.html'
    form_class = FeedbackForm
    ordering = ['-posted_on']

    def form_valid(self, form):
        form.instance.course_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk':self.kwargs['pk']})