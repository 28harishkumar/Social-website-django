from django.shortcuts import render , render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse , Http404
from django.core.urlresolvers import reverse
from django.views.generic import View
from user.models import User
    
class ShowMessage(View):
    #show list of user messages, i.e., users with latesr messages
    pass

class ShowUserMessage(View):
    #show all messages for a single user
    pass

class CreateMessage(View):
    #send a new message
    pass

class DeleteMessage(View):
    #delete message
    pass

class DeleteBulkMessage(View):
    #delete selected messages
    pass

class DeleteAllMessage(View):
    #delete all message for a user
    pass
    