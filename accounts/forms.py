from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms


class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        if email and User.objects.filter(email=email).exists():
            raise ValidationError("This email or username is already taken.")
        return email
        

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class CustomAuthenticationForm(AuthenticationForm):

    captcha = CaptchaField()

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password."
        ),
        "inactive": _("This account is inactive."),
    }
