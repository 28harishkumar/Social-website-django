from django.db import models
from user.models import User
# Create your models here.
class Post(models.Model):
    
    types = (
             ('img','Image'),
             ('video','Video'),
             ('pdf','PDF File'),
             ('audio','Audio File'),
             ('txt','Text File'),
             ('url','Link'),
             )
    
    user_id = models.ForeignKey(User)
    status = models.TextField(null=True,blank = True)
    attachment_type = models.CharField(choices = types, null = True, blank = True, max_length = 10)
    attachment = models.CharField(null = True, blank = True, max_length = 250)
    like = models.ManyToManyField(User, related_name = 'liked_post', null = True, blank = True)
    favorite = models.ManyToManyField(User, related_name = 'favorite_post', null = True, blank = True)
    root_post = models.ForeignKey('self', null = True, blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_id.first_name