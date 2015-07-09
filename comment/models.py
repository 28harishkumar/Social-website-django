from django.db import models
from user.models import User
from post.models import Post

# Create your models here.

class Comment(models.Model):
    user_id = models.ForeignKey(User)
    post_id = models.ForeignKey(Post)
    comment = models.CharField(max_length = 250)
    on_comment = models.ForeignKey('self',related_name = 'reply',null = True, blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment