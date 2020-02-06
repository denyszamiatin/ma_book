from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="receiver")
    message = models.TextField(max_length=3000)
    send_date = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
