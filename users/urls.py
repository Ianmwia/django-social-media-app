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
    path("api/", include(router.urls)),
    
    #path("register", views.register, name='register'),
    path("", views.landing_page, name='home'),
    path("register", views.register, name='register'),

    

    #django auth login logout
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LoginView.as_view(template_name='logout.html'), name='logout'),
]