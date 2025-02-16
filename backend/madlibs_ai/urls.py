from django.contrib import admin
from django.urls import path, include
from apps.game.views import RandomTemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.api.urls')),
]
