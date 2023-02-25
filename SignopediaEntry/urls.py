from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

from SignopediaEntry import views

urlpatterns = [
    path('model/', views.call_model.as_view())
]