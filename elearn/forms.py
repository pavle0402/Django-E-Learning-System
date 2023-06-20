from django import forms
from .models import User, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django_countries.data import COUNTRIES
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.forms import ValidationError

genders = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class StudentSignupForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length= 155, widget=forms.TextInput(attrs={"class":"form-control-sm",
                                                                                "placeholder":"Enter your first name."}))
    last_name = forms.CharField(required=True, max_length= 155, widget=forms.TextInput(attrs={"class":"form-control-sm",
                                                                                "placeholder":"Enter your last name."}))
    username = forms.CharField(required=True, max_length= 155, widget=forms.EmailInput(attrs={"class":"form-control-sm",
                                                                           "placeholder":"Enter your email(username)."}))
    phone_number = forms.CharField(required=True, max_length= 15, widget=forms.NumberInput(attrs={"class":"form-control-sm",
                                                                           "placeholder":"Enter your phone number."}))
    password1 = forms.CharField(required=True, max_length=155, widget=forms.PasswordInput(attrs={"class":"form-control-sm",
                                                                            "placeholder":"Enter your password."}))
    password2 = forms.CharField(required=True, max_length=155, widget=forms.PasswordInput(attrs={"class":"form-control-sm",
                                                                            "placeholder":"Confirm your password."}))
    gender = forms.CharField(required=True, widget=forms.Select(choices=genders, attrs={"class":"form-control-sm"}))
    city = forms.CharField(required=True)
    country = forms.CharField(required=True, widget=forms.Select(choices=sorted(COUNTRIES.items())))


    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'password1', 'password2', 'phone_number', 'gender', 'country', 'city') 






    # def clean_username(self):
    #     clean_username = self.username.cleaned_data()
    #     if "@" in clean_username:
    #         try:
    #             clean_username = CustomUser.objects.get(email=clean_username).username
    #         except ObjectDoesNotExist:
    #             raise ValidationError(
    #                 f"{self.username} is not correct username.",
    #                 params={'username':self.username.verbose_name},
    #             )
            
    #     return clean_username


  
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_pic', 'birth_date')

        widgets = {
        'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'my-textarea-class', 'placeholder':'Interests, hobbies, why are u here...'}),
        'profile_pic': forms.ClearableFileInput(attrs={'class': 'my-file-input-class', 'help_text':'Please use picture of yourself.'}),
        'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'my-date-input-class', 'class':'Enter your birth date.'}),
        }
    

# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = CourseFeedback
#         fields = ('name', 'comment')

#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-class', 'placeholder':'Enter your name. Not required.'}),
#             'comment': forms.Textarea(attrs={'class':'form-class', 'placeholder':'Share your opinion on this course...'})
#         }