"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from .api.views import MessageViewSet
# from .api.views import index_view
from .api.experiences.views import ExperienceViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('experiences', ExperienceViewSet, base_name="Experience")
router.register('tags', TagViewSet, base_name="Tag")
# router.register('comments', CommentViewSet, basename="comments")

urlpatterns = [

    # http://localhost:8000/
    # path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('admin/', admin.site.urls),

    # regsiter new user
    path('api/accounts/registration/', include('rest_auth.registration.urls')),
    
    # login and logout
    path('api/accounts/', include('rest_auth.urls')),

    # update user settings an d profile
    path('api/accounts/', include('backend.api.accounts.urls')),

    path('api-auth/', include('rest_framework.urls')),

    path('api/comments/', include('backend.api.experiences.urls')),

    path('', TemplateView.as_view(template_name='index.html'))
]