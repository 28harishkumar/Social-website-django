from django.shortcuts import render , render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse , Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import JsonResponse
from user.models import User
from post.models import Post
from comment.models import Comment
from post.forms import PostCreateForm

class CreatePost(View):
    @method_decorator(login_required)
    def post(self,request):
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return render_to_response('ajax_responses/post-saved.html',
                                       context_instance=RequestContext(request))
        else:
            return render_to_response('ajax_responses/post-failed.html',
                                      {'form':form},
                                       context_instance=RequestContext(request))

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

class PostComments(View):
    @method_decorator(login_required)
    def get(self,request,post_id):
        comments = get_object_or_404(Post, pk = post_id).comment_set.all()        
        return render_to_response('ajax_responses/comment_list.html',
                                  {'comments':comments},
                                  context_instance=RequestContext(request))
        
    
    
    
    