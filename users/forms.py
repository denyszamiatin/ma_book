from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'example@mail.com'
                                                                           }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'password'
                                                                                 }))
    password2 = forms.CharField(label="Password confirm",widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'confirm password'
                                                                                 }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
