from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

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

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
        
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('profile')
    else:
        user_form =CustomUserCreationForm()
        profile_form = ProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

#profile page and edit
@login_required
def profile_page(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile_page.html', {'profile':profile})

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        profile.bio = request.POST.get('bio')
        profile.save()
    return render(request, 'profile_page.html', {'profile':profile})