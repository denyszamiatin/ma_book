from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=150, required=True, widget=forms.TextInput())
    text = forms.CharField(widget=forms.Textarea())


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title', 'text'
        widgets = {
            'title': forms.TextInput(),
        }