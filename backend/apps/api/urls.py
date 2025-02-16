# api/urls.py
from django.urls import path
from .views import MadlibsAPIView

urlpatterns = [
    path('madlibs/', MadlibsAPIView.as_view(), name='madlibs_api'),
]