from django.urls import path
from .views import register_view, profile_view, logout_view, login_view, session_view, dashboard_view
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='dashboard'), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/password_change.html',
            success_url=reverse_lazy('dashboard')   # ✅ dashboard redirect after change
        ),
        name='password_change'
    ),
    path('session/', session_view, name='session_info'),

]



urlpatterns += [

    # 1 email input
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.html',
            success_url=reverse_lazy('password_reset_done')
        ),
        name='password_reset'
    ),

    # 2 email sent page
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    # 3 set new password
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url=reverse_lazy('password_reset_complete')
        ),
        name='password_reset_confirm'
    ),

    # 4 success page
    path(
        'reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]