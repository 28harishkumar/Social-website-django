from django.forms import ModelForm
from django import forms
from comment.models import Comment

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user','comment','post','on_comment']
        exclude = ['created_on']

class CommentUpdateForm(ModelForm):
        
    class Meta:
        model = Comment
        fields = ['user','comment','post']
        exclude = []
