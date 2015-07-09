from django.shortcuts import render , render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse , Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View
from user.models import User
from post.models import Post
from comment.models import Comment
from message.models import Message
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
    
class Home(View):
    @method_decorator(login_required)
    def get(self,request):
        return render_to_response('home.html', context_instance=RequestContext(request))
    
class Login(View):
    def get(self,request):
        next = request.GET.get('next','/')
        if request.user.is_authenticated():
            return HttpResponseRedirect(next)
        form = UserCreationForm()
        return render_to_response('login.html', {'form':form,'next': next}, context_instance=RequestContext(request))
    
    def post(self,request):
        pass

class Timeline(View):
    pass

class Profile(View):
    pass

class TimelineStatus(View):
    pass

class TimelineImage(View):
    pass

class TimelineVideo(View):
    pass

class Activity(View):
    pass

class Like(View):
    pass

class Favorite(View):
    pass

class FavoriteStatus(View):
    pass

class FavoriteVideo(View):
    pass

class FavoriteImage(View):
    pass

class FavoriteAudio(View):
    pass

class Settings(View):
    pass