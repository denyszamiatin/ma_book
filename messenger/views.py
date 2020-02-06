from django.shortcuts import redirect, reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import User, Messages
from .forms import MessageForm
from django.contrib import messages


@login_required
def send(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        receiver = User.objects.get(username=request.POST.get('receiver'))
        if form.is_valid():
            sender = User.objects.get(username=request.user.username)
            message = Messages(sender=sender, receiver=receiver, message=form.cleaned_data['users_message'])
            message.save()
            messages.success(request, f'Message sent to {receiver.username}')
            return redirect(reverse('users:profile', args=(receiver.username,)))
        messages.error(request, 'Invalid input')
        return redirect(reverse('users:profile', args=(receiver.username,)))
    raise Http404("Page does not exist")
