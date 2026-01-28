from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'w-full outline rounded mb-1 p-1 bg-white'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'w-full outline rounded mb-1 p-1 bg-white'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'w-full outline rounded mb-1 p-1 bg-white'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'w-full outline rounded mb-1 p-1 bg-white'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full outline rounded mb-1 p-1 bg-white'
        })
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
         # Validation
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists')
        return email
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']
