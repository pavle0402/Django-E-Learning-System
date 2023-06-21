from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('services/', views.services_page, name='services'),
    path('privacy_policy/', views.policy_page, name='policy'),
    path('', views.contact_page, name='contact'),
    path('instructors/', views.InstructorsView, name='instructors'),
    path('student_signup/', views.SignupStudentView, name='student_signup'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('course_list/', views.CourseListView.as_view(), name='course_list'),
    path('course_detail/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('announcements/', views.AnnouncementView.as_view(), name='announcements'),
    path('create_announcement/', views.CreateAnnouncementView.as_view(), name='create_announcement'),
    path('<int:pk>/update', views.UpdateAnnouncementView.as_view(), name='update_announcement'),
    path('<int:pk>/delete', views.DeleteAnnouncementView.as_view(), name='delete_announcement'),
    path('create_profile/', views.ProfileCreateView.as_view(), name='create_profile'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_page'),
    path('course_detail/<int:course_id>/enroll/', views.EnrollCourseView.as_view(), name='enroll'),
    path("course_detail/<int:pk>/feedback/", views.FeedbackCreateView.as_view(), name='feedback'),

]