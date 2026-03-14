from django.urls import path
from .views import dashboard_view, home

urlpatterns = [
    # Codeforces User Info dekhbar link
    path('dashboard/', dashboard_view, name='cf_activity'),
    path('home/', home, name='home'),
]
