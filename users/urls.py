from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

#serializers router path
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()
router.register(r'', views.ProfileViewSet, basename='profile')

urlpatterns = [
    #api router urls
    path("", include(router.urls)),

    #path("register", views.register, name='register'),
    path("", views.landing_page, name='home'),
    path("register", views.register, name='register'),
]