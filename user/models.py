from django.db import models
from django.contrib.auth.models import AbstractUser
from sorl.thumbnail import ImageField
# Create your models here.

class User(AbstractUser,models.Model):
    AbstractUser._meta.get_field('email')._unique = True
    confirmation_code = models.CharField(max_length=34,null = True,blank = True)
    followers = models.ManyToManyField('self', 
                                       symmetrical=False,
                                       related_name = 'following') 
    profile_photo = ImageField(upload_to = 'user/profile', default = 'user/profile/default_profile.jpg')
    cover_image = ImageField(upload_to = 'user/cover', default = 'user/cover/default_cover.jpg')
    
    REQUIRED_FIELDS = ('email','first_name')
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username
    
    def name(self):
        return '%s %s' % (self.first_name,self.last_name)
    
    class Meta:
            db_table = 'auth_user'

"""
following followers
quote

email
website
live in 
studied at
work at


date of birth
gender
language
Joined on
"""

class City(models.Model):
    
    region_choices = (
          ('AS','Asia'),
          ('Af','Africa'),
          ('EU','Europe'),
          ('NA','North Amarica'),
          ('SA','South Amarica'),
                      )
    
    country_choices = (
                       ('IND','India'),
                       )
    name = models.CharField(max_length = 100)
    country = models.CharField(max_length = 3, choices = country_choices)
    region = models.CharField(max_length = 2, choices = region_choices)  
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural = 'Cities'

class Profile(models.Model):
    
    sex_choices = (
            ('m','MALE'),
            ('f','FEMALE'),
            ('n','NONE')       
                   )
    
    language_choices = (
                        ('ENG', 'English'),
                        ('HIN','Hindi'),
                        )
    
    user = models.OneToOneField(User)
    live_in = models.ForeignKey(City, null = True, blank = True)
    work_at = models.CharField(max_length = 100, null = True, blank = True)
    website = models.URLField(null = True, blank = True)
    data_of_birth = models.DateField(null = True, blank = True)
    gender = models.CharField(max_length = 1, choices = sex_choices, null = True, blank = True)
    language = models.CharField(max_length = 5, choices = language_choices, null = True, blank = True)
    quote = models.CharField(max_length = 200, null = True, blank = True)
    
    def __str__(self):
        return self.user.username
    



