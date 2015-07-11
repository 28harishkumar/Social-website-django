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
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
        AdminPasswordChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
    
class Home(View):
    @method_decorator(login_required)
    def get(self,request):
        posts = Post.objects.order_by('-created_on')
        return render_to_response('home.html', 
                                  {'posts':posts},
                                  context_instance=RequestContext(request))
    
class Login(View):
    
    def reset_session_errors(self, request):
         try:
            del request.session['errors']
         except KeyError:
            pass
        
    def get(self,request):
        next = request.GET.get('next','/')
        if request.user.is_authenticated():
            return HttpResponseRedirect(next)
        form = AuthenticationForm()
        return render_to_response('registration/login.html', 
                                  {'form':form,'next': next}, 
                                  context_instance=RequestContext(request))
    
    def post(self,request):
        self.reset_session_errors(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                request.session['errors'] = ['your account is not activated']
                return HttpResponseRedirect('/')
        else:
            request.session['errors'] = ['Invalid username and password combination',]
            return HttpResponseRedirect('/')

class Logout(View):
    def get(self,request):
        if request.user.is_authenticated():
            logout(request)
        return HttpResponseRedirect('/')

class PasswordChange(View):
    @method_decorator(login_required)
    def get(self,request):
        form = PasswordChangeForm(request.user)
        return render_to_response('registration/password_change_form.html', 
                                  {'form':form}, 
                                  context_instance=RequestContext(request))
    
    @method_decorator(login_required)
    def post(self,request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            HttpResponseRedirect('/')
        else:
            return render_to_response('registration/password_change_form.html', 
                                      {'form':form}, 
                                      context_instance=RequestContext(request))

class PasswordReset(View):
    def get(self,request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        form = PasswordResetForm()
        return render_to_response('registration/password_reset_form.html', 
                                  {'form':form}, 
                                  context_instance=RequestContext(request))
    
    def post(self,request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            form.save()
            HttpResponseRedirect('/')
        return render_to_response('registration/password_reset_form.html', 
                                  {'form':form}, 
                                  context_instance=RequestContext(request))


class SetPassword(View):
    def get(self,request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        form = SetPasswordForm()
        return render_to_response('registration/set_password_form.html', 
                                  {'form':form}, 
                                  context_instance=RequestContext(request))
    
    def post(self,request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        form = SetPasswordForm(data=request.POST)
        if form.is_valid():
            form.save()
            HttpResponseRedirect('/')
        return render_to_response('registration/set_password_form.html', 
                                  {'form':form}, 
                                  context_instance=RequestContext(request))

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