from django.contrib import admin
from post.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    list_display = ('user_id','id')
    search_fields = ('user_id', 'id', 'status')

    fieldsets = (
        (None, {'fields': ('user_id', 'status')}),
        ('Attachment', {'fields': ('attachment_type', 'attachment')}),
        ('social',{'fields':('like','favorite','root_post')}),
    )
    
admin.site.register(Post,PostAdmin)
