from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=150, required=True, widget=forms.TextInput())
    text = forms.CharField(widget=forms.Textarea())
    image = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'custom-file-input',
                                                             'id': 'post_image_input'
                                                             }))


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title', 'text', 'image'
        widgets = {
            'title': forms.TextInput(),
            'text': forms.Textarea(),
            'image': forms.FileInput()
        }


class HashTagForm(forms.Form):
    hash_tags = forms.CharField(max_length=150, required=False, widget=forms.TextInput(
                            attrs={'placeholder': '#python #django'}))
