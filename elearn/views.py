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
from django.core.mail import send_mail, BadHeaderError
from django.contrib import auth
from datetime import datetime, date
from django.core.exceptions import ValidationError
from django.db.models import Avg, Count, Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm)
from .models import (User, Course, Announcement, UserProfile, Feedback)
from .forms import (StudentSignupForm, CreateProfileForm, FeedbackForm, EditProfileForm, ContactForm)
from django.contrib.auth.decorators import login_required



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

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            topic = form.cleaned_data('topic')
            email = form.cleaned_data('email')
            question = form.cleaned_data('content')
            try:
                send_mail(topic, question, email,['pavles2002@gmail.com'])
                messages.success(request, "You have successfully sent your inquiry.")
            except BadHeaderError:
                raise BadHeaderError("Invalid header found.")
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form':form})

def services_page(request):
    return render(request, 'services.html', {})

def policy_page(request):
    return render(request, 'policy.html', {})

def contact_page(request):
    return render(request,'contact.html', {})

def InstructorsView(request):
    return render(request, 'instructors.html', {})


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
    

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

# def course_payment(request):
#     return render(request, 'payment.html', {})

class CourseListView(ListView):
    model = Course
    queryset = Course.objects.all()
    template_name = "course_list.html"
    # context_object_name = "course"
    
class CourseDetailView(DetailView):     
    model = Course
    context_object_name = 'course'
    template_name = 'course_detail.html'
    ordering = ['feedbacks']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedbacks = Feedback.objects.filter(course=self.object)
        print('feedbacks', feedbacks)
        average_rating = feedbacks.aggregate(Avg('ratings'))['ratings__avg']
        print("average_ratings", average_rating)
        context['feedbacks'] = Feedback.objects.filter(course=self.object)
        context['average_rating'] = average_rating

        return context

class EnrollCourseView(View):
    def get(self, request, *args, **kwargs):
        return reverse_lazy('course_detail', pk=self.kwargs['course_id'])
    
    def post(self ,request, *args, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs['course_id'])
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile:
            if course not in user_profile.enrolled_courses.all():
                user_profile.enrolled_courses.add(course)
                messages.success(request,f"You have successfully enrolled for {course.name}. Good luck!")
                return redirect('course_list')
            else:
                messages.warning(request,f"You are already enrolled in {course.name}.")
                return redirect('course_list')
        else:
            messages.warning(request,"You must create account and profile first.")
            return redirect('register')
        


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

class ProfileListView(ListView):
    model = UserProfile
    template_name = "profiles_list.html"
    context_object_name = "profile"


#profile views
class ProfileCreateView(CreateView):
    model = UserProfile
    template_name = "create_profile.html"
    form_class = CreateProfileForm
    success_url = reverse_lazy('home')    
    # def get_success_url(self):
    #     return reverse_lazy('profile_page', kwargs={'pk':self.kwargs['pk']})

# for staff only
class DeleteProfilView(DeleteView):
    model = UserProfile
    template_name = "delete_profile.html"
    success_url = reverse_lazy("profile_list")


class ProfileDetailView(DetailView):
    model = UserProfile 
    context_object_name = "userprofile"
    template_name = "user_profile.html"

class ProfileEditView(UpdateView):
    model = UserProfile
    template_name = "edit_profile.html"
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse_lazy('profile_page', kwargs={'pk': self.kwargs['pk']})
    


#feedback
class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    ordering = ['-posted_on']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.course_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk':self.kwargs['pk']})
    
    def get_template_names(self):
        template_names = [
            'add_feedback.html',
        ]
        return template_names