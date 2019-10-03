"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    # main page index
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    # admin dashboard
    path('admin/', admin.site.urls),

    # regsiter new user
    path('api/accounts/registration/', include('rest_auth.registration.urls')),
    
    # login and logout
    path('api/accounts/', include('rest_auth.urls')),

    # update user settings an d profile
    # path('api/accounts/', include('backend.api.accounts.urls')),

    path('api-auth/', include('rest_framework.urls')),

    # path('api/comments/', include('backend.api.experiences.urls')),
]