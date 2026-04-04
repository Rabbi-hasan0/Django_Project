from django.urls import path
from .views import *

urlpatterns = [
    path('post/', details1),
    path('home/', details2),
]
