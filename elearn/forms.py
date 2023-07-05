from django import forms
from .models import User, UserProfile, Feedback
from django.contrib.auth.forms import UserCreationForm
from django_countries.data import COUNTRIES
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.forms import ValidationError
from django.forms.widgets import RadioSelect

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
        fields = ('bio', 'profile_pic', 'birth_date', 'user', 'instagram', 'facebook', 'twitter', 'linkedin')

        widgets = {
        'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'my-textarea-class', 'placeholder':'Interests, hobbies, why are u here...'}),
        'profile_pic': forms.ClearableFileInput(attrs={'class': 'my-file-input-class', 'help_text':'Please use picture of yourself.'}),
        'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'my-date-input-class', 'class':'Enter your birth date.'}),
        'user': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'owner', 'type':'hidden'}),
        }
    

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_pic', 'birth_date','instagram', 'facebook', 'twitter', 'linkedin')

        widgets = {
        'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'my-textarea-class', 'placeholder':'Interests, hobbies, why are u here...'}),
        'profile_pic': forms.ClearableFileInput(attrs={'class': 'my-file-input-class', 'help_text':'Please use picture of yourself.'}),
        'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'my-date-input-class', 'class':'Enter your birth date.'}),
        'instagram': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Enter your instagram url.'}),
        'twitter': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Enter your instagram url.'}),
        'facebook': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Enter your instagram url.'}),
        'linkedin': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Enter your instagram url.'}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('content','author', 'ratings')

        star_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        )

        widgets = {
            'content': forms.Textarea(attrs={'class':'form-control', 'rows':6, 'cols': 30, 'placeholder':'Give us your honest review for this course!'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'type':'hidden', 'id':'author'}),
            'ratings': forms.RadioSelect(choices=star_choices, attrs={'class':'form-check-inline'}),

        }
        

class ContactForm(forms.Form):
    topic = forms.CharField(label='Topic',required=True) #Make this choice field with choices such as: payment, enrollment and idk what else, figure it out, this is just temporary
    email = forms.EmailField(label='E-mail:', required=True)
    content = forms.CharField(label='Question', required=True)

    widgets = {
        'topic': forms.TextInput(attrs={'class':'form-control', 'placeholder':'What do you wanna ask about?'}),
        'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your personal e-mail...'}),
        'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ask us anything...'})
    }

    def clean_email(self):
        email_form = ContactForm.cleaned_data('email')
        if "@" in email_form and email_form.endswith('.com'):
            pass
        else:
            raise ValueError("Incorrect form of e-mail, enter the right information please.")