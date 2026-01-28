from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import login, logout
#serializers for api endpoints
from rest_framework import viewsets
from .models import Profile
from .serializers import ProFileSerializer


#class based api views
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProFileSerializer



# Create your views here.
def landing_page(request):
    return render(request, 'landing.html')

# register
def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid():
            user = user_form.save()
        
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('landing')
    else:
        user_form =CustomUserCreationForm()
        profile_form = ProfileForm()

    return render(request, 'register.html', {'user_form': user_form})