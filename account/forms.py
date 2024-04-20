from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

        # prevent existing email

    def clean_email(self):
        data = self.cleaned_data["email"]

        # Check if the user being edited is available
        if hasattr(self, 'instance') and self.instance.id:
            users = User.objects.filter(email=data).exclude(id=self.instance.id)
        else:
            users = User.objects.filter(email=data)

        if users.exists():
            raise forms.ValidationError("This email address is already used")

        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data["email"]

        # Check if the user being edited is available
        if hasattr(self, 'instance') and self.instance.id:
            users = User.objects.filter(email=data).exclude(id=self.instance.id)
        else:
            users = User.objects.filter(email=data)

        if users.exists():
            raise forms.ValidationError("This email address is already used")

        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', "photo"]
