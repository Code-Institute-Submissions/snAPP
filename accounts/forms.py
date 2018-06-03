from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



# Registration
class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""
    
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput)
    
    password2 = forms.CharField(
        label="Password Confirmation", 
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'This email address is currently registered to another snAPP member.')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Your passwords do not match. Please try again.")
        
        return password2

# Login
class UserLoginForm(forms.Form):
    """Forms to be used to log users in"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Edit User Profile
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'alert')