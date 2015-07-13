from django.forms import ModelForm
from django import forms
from post.models import Post

class PostCreateForm(ModelForm):
    
    image_types = ('jpg','png','jpeg')
    video_types = ('mp4','flv','avi')
    audio_types = ('mp3',)
    file_types = ('pdf','cvs','txt')
    blocked_types = ('exe','sh')
    
    class Meta:
        model = Post
        fields = ['user','status','attachment','attachment_type','root_post']
        exclude = ['like','favorite']
    
    def clean_attachment_type(self):
        attachment = self.cleaned_data['attachment']
        attachment_type = self.cleaned_data['attachment_type']
        if attachment:
            ext = attachment.name.split('.')[-1]
            if(ext in self.image_types):
                attachment_type = 'image'
            elif(ext in self.video_types):
                attachment_type = 'video'
            elif(ext in self.audio_types):
                attachment_type = 'audio'
            elif(ext in self.file_types):
                attachment_type = 'file'
            else:
                raise forms.ValidationError('Invalid type attachment')
        return attachment_type
        
    def clean(self):
        super(PostCreateForm, self).clean()
        attachment = self.cleaned_data['attachment']
        status = self.cleaned_data['status']
        root_post = self.cleaned_data['root_post']
        if attachment == None and status.strip() == '' and root_post == None:
            raise forms.ValidationError('status can not be empty')
        