from django.forms import ModelForm
from django import forms
from comment.models import Comment

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user','comment','post','on_comment']
        exclude = ['created_on']

class CommentUpdateForm(ModelForm):
    
    def __init__(self, comment_id, *args, **kwargs):
        self.comment_id = comment_id
        super(CommentUpdateForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Comment
        fields = ['id','user','comment','post','on_comment']
        exclude = ['created_on']
