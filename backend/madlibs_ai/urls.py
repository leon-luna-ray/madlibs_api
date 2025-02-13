from django.contrib import admin
from django.urls import path
from django.urls import path
from django.views.generic import TemplateView
from apps.game.views import RandomTemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/random/', RandomTemplateView.as_view(), name='random'),
]
