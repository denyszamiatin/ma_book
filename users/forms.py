from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'John'
                                                                              }))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Smith'
                                                                              }))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'your unique login'
                                                                             }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'example@mail.com'
                                                                           }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'password'
                                                                                    }))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'password'
                                                                                    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                             'placeholder': '31.12.1992'
                                                             }))
    avatar = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'custom-file-input',
                                                             'id': 'avatar_input'
                                                             }))

    class Meta:
        model = UserProfile
        fields = ('birthday', 'avatar')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Your name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Your password'}))


class SearchForm(forms.Form):
    username = forms.CharField(max_length=150, required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=150, required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=150, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    email = forms.CharField(max_length=150, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    birthday = forms.DateField(required=False,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': '16.10.1994'}))


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email'


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = 'birthday', 'status'


class EditUserAvatar(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
