from django.shortcuts import render , render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse , Http404
from django.core.urlresolvers import reverse
from django.views.generic import View
from user.models import User
from post.models import Post
    
class CreateComment(View):
    pass

class EditComment(View):
    pass

class UpdateComment(View):
    pass

class DeleteComment(View):
    pass
