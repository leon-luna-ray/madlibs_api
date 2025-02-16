from django.urls import path
from .views import StoriesAPIView

urlpatterns = [
    path('/', StoriesAPIView.as_view(), name='stories'),
]