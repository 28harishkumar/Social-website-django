from django.db import models
from user.models import User
# Create your models here.
class Message(models.Model):
    sender_id = models.ForeignKey(User,related_name = 'sended_message')
    receiver_id = models.ForeignKey(User,related_name = 'received_message')
    is_read = models.BooleanField(default=False)
    receiver_deleted = models.BooleanField(default = False)
    sender_deleted = models.BooleanField(default = False)
    created_on = models.DateTimeField(auto_now_add=True)