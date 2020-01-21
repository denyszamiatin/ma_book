from django import forms
from .models import Gallery


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = 'image', 'about'
