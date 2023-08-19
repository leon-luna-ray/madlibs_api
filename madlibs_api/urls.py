from django.contrib import admin
from django.urls import path
from game.views import RandomTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/random/', RandomTemplateView.as_view(), name='random'),
]
