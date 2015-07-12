from django.shortcuts import render , render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse , Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View
from user.models import User
from post.models import Post
from comment.models import Comment
from comment.forms import CommentCreateForm, CommentUpdateForm
    
class CreateComment(View):
    @method_decorator(login_required)
    def post(self,request):
        form = CommentCreateForm(data=request.POST)   
        if form.is_valid():
            form.user = request.user
            form.save()
            return HttpResponse('success')
        else:
            raise Http404()

class UpdateComment(View):
    @method_decorator(login_required)
    def post(self,request,comment_id):
        comment = get_object_or_404(Comment, pk = comment_id)
        if(comment.user == request.user):
            data = request.POST.copy()
            data['user'] = request.user.id
            data['post'] = comment.post.id
            data['id'] = comment.id          
            form = CommentUpdateForm(data=data, instance = comment)
            if form.is_valid():
                form.save()
                return HttpResponse('success')
        raise Http404('invalid form')

class DeleteComment(View):
    @method_decorator(login_required)
    def post(self,request,comment_id):
        comment = get_object_or_404(Comment, pk = comment_id)
        if comment.user.id == request.user.id and comment.id == int(comment_id):
            comment.delete()
            return HttpResponse('success')
        else:
            raise Http404()
            
            
            
            
            
            
