from django.shortcuts import render , render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse , Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View
from user.models import User
from post.models import Post
from comment.forms import CommentCreateForm
    
class CreateComment(View):
    @method_decorator(login_required)
    def post(self,request):
        form = CommentCreateForm(data=request.POST)   
        if form.is_valid():
            form.user = request.user
            form.save()
            return HttpResponse('success')
        else:
            return Http404

class EditComment(View):
    pass

class UpdateComment(View):
    pass

class DeleteComment(View):
    pass
