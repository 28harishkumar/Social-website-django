from django.forms import ModelForm
from django import forms
from post.models import Post

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user','status','attachment_type','attachment','root_post']
        exclude = ['like','favorite']
    
    def clean(self):
        super(PostCreateForm, self).clean()
        attachment = self.cleaned_data['attachment']
        status = self.cleaned_data['status']
        root_post = self.cleaned_data['root_post']
        if attachment == '' and status.strip() == '' and root_post == None:
            raise forms.ValidationError('status can not be empty')
        