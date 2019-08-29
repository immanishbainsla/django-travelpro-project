from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile, ContactModel
from django.contrib.auth.models import User



# default User Form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


# Custom fields for User
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'current_address', 'parmanent_address', 'age', 'portfolio_site')


# Contact form for everyone
class UserContactForm(forms.ModelForm):

    class Meta():
        model = ContactModel
        fields = ('name', 'email', 'query')
