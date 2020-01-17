from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title', 'text'