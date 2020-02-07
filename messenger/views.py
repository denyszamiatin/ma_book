from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Messages
from .forms import MessageForm


@login_required
def send(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        receiver = User.objects.get(username=request.POST.get('receiver'))
        if form.is_valid():
            sender = User.objects.get(username=request.user.username)
            message = Messages(sender=sender, receiver=receiver, message=form.cleaned_data['users_message'])
            message.save()
            previous_page = request.POST.get('redirect_to')
            if previous_page == 'dialogue':
                return redirect(reverse('messenger:dialogue', args=(receiver.username,)))
            else:
                messages.success(request, f'Message sent to {receiver.username}')
                return redirect(reverse('users:profile', args=(receiver.username,)))
        messages.error(request, 'Invalid input')
        return redirect(reverse('users:profile', args=(receiver.username,)))
    raise Http404("Page does not exist")


@login_required
def dialogs(request):
    dialogs_ = Messages().get_dialogs(request.user.id)
    return render(request, 'dialogs.html', {'dialogs': dialogs_})


@login_required
def dialogue(request, username):
    form = MessageForm()
    second_user = get_object_or_404(User, username=username)
    users_dialogue = Messages().get_messages(request.user.id, second_user.id)
    return render(request, 'dialogue.html', {"users_messages": users_dialogue, "form": form, 'send_to': username})
