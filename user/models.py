from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser,models.Model):
    AbstractUser._meta.get_field('email')._unique = True
    confirmation_code = models.CharField(max_length=34,null = True,blank = True)
    followers = models.ManyToManyField('self', related_name = 'following') 
#     profile_photo = models.ImageField(upload_to = 'user/profile',null = True,blank = True)
#     cover_image = models.ImageField(upload_to = 'user/cover',null = True,blank = True)
    
    REQUIRED_FIELDS = ('email','first_name')
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username
    
    def name(self):
        return '%s %s' % (self.first_name,self.last_name)
    
    class Meta:
            db_table = 'auth_user'
