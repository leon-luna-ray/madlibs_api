from django.contrib import admin
from django.urls import path
from django.urls import path
from django.views.generic import TemplateView
from game.views import RandomTemplateView

urlpatterns = [
#  path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('admin/', admin.site.urls),
    path('api/random/', RandomTemplateView.as_view(), name='random'),
]
