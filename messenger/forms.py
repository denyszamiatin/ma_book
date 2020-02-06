from django import forms


class MessageForm(forms.Form):
    users_message = forms.CharField(required=True, max_length=5000,
                                    widget=forms.TextInput(attrs={'class': 'message-form'}))

