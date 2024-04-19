from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('about/', views.view_about, name='view_about'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('venues/', views.venues, name='venues'),
    path('courses/', views.view_courses, name='view_courses'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)