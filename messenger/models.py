from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Q


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="receiver")
    message = models.TextField(max_length=3000)
    send_date = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def get_dialogs(self, current_user_id):
        """
        :param current_user_id: id of logined user
        :return: list of User objects witch have opened dialogue with current user
        """
        dialogs = Messages.objects.filter(Q(sender=current_user_id) |
                                          Q(receiver=current_user_id)).values('sender', 'receiver').distinct()
        dialogue_participants = [(dialog['sender'], dialog['receiver']) for dialog in dialogs]
        for i, pair in enumerate(dialogue_participants):
            if pair[::-1] in dialogue_participants[i:]:
                dialogue_participants.pop(dialogue_participants.index(pair[::-1]))
        users = [item for pair in dialogue_participants for item in pair if item != current_user_id]
        return [User.objects.get(pk=id_) for id_ in users]

    def get_messages(self, first_id, second_id):
        """
        :param first_id: id of first dialogue participant
        :param second_id: id of second dialogue participant
        :return: Query set of messages from first user to second and from second to first
        """
        return Messages.objects.filter((Q(sender=first_id) & Q(receiver=second_id)) |
                                        (Q(sender=second_id)) & Q(receiver=first_id)).order_by('send_date')
