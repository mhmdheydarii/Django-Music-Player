from django.urls import path, include
from . import views

app_name = 'accounts'


urlpatterns = [
    # registration
    path('signup/', views.SignupView.as_view(), name='signup'),
    # login
    path('login/',views.CustomLoginView.as_view(), name='login'),
    # logout
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    # change password
    path('change-password/', views.CustomChangePasswordView.as_view(), name='change-password'),
    # reset password
    path('reset-password/', views.CustomPasswordResetView.as_view(), name='reset-password'),
    path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password-reset-done'),
]