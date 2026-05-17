from django.views.generic import FormView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
)
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import SignUpForm, CustomAuthenticationForm

# Create your views here.


class SignupView(FormView):

    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("music:index")

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
                return redirect("accounts:signup")
        return super().form_valid(form)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Account created successfully")
        return redirect(self.success_url)


class CustomLoginView(LoginView, FormView):

    form_class = CustomAuthenticationForm
    template_name = "registration/login.html"

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
                return redirect("accounts:login")
        return super().form_valid(form)



class CustomLogoutView(LogoutView):

    template_name = "music/index.html"



class CustomChangePasswordView(PasswordChangeView):

    template_name = "registration/change_password.html"
    success_url = reverse_lazy("music:index")

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
        return super().form_invalid(form)


class CustomPasswordResetView(PasswordResetView):
    template_name = "registration/password_reset.html"
    success_url = reverse_lazy("accounts:password-reset-done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/password-reset-done.html"