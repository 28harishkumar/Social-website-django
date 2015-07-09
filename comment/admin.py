from django.contrib import admin
from comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('user_id','post_id','comment')
    
admin.site.register(Comment,CommentAdmin)