from django.contrib import admin
from comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('user','post','comment')
    
admin.site.register(Comment,CommentAdmin)