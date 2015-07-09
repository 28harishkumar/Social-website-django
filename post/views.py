from django.shortcuts import render , render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse , Http404
from django.core.urlresolvers import reverse
from django.views.generic import View
from user.models import User
from comment.models import Comment

class CreatePost(View):
    #add new post
    pass

class EditPost(View):
    #edit post
    pass

class UpdatePost(View):
    #update post
    pass

class DeletePost(View):
    #delete post
    pass

class ShowPost(View):
    #show post
    pass
    