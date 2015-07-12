from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from user.views import *
from post.views import *
from message.views import *
from comment.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',Home.as_view(),name='index'),
    
    url(r'^accounts/login/$',Login.as_view(),name='login'),
    url(r'^accounts/logout/$',Logout.as_view(),name='logout'),
    url(r'^accounts/password_reset/$',PasswordReset.as_view(),name='password_reset'),
    url(r'^accounts/set-password/$',SetPassword.as_view(),name='set_password'),
    url(r'^accounts/password_change/$',PasswordChange.as_view(),name='password_change'),
    
    url(r'^(?P<user>[0-9]+)$', Timeline.as_view(), name = 'timeline'),
    url(r'^(?P<user>[0-9]+)/profile$', Profile.as_view(), name='profile'),
    url(r'^(?P<user>[0-9]+)/status$',TimelineStatus.as_view()),
    url(r'^(?P<user>[0-9]+)/image$',TimelineImage.as_view()),
    url(r'^(?P<user>[0-9]+)/video$',TimelineVideo.as_view()),
    url(r'^(?P<user>[0-9]+)/activity$',Activity.as_view()),
    url(r'^(?P<user>[0-9]+)/likes$',Like.as_view()),
    
    url(r'^(?P<user>[0-9]+)/favorite$',Favorite.as_view()),
    url(r'^(?P<user>[0-9]+)/favorite/status$',FavoriteStatus.as_view()),
    url(r'^(?P<user>[0-9]+)/favorite/video$',FavoriteVideo.as_view()),
    url(r'^(?P<user>[0-9]+)/favorite/image$',FavoriteImage.as_view()),
    url(r'^(?P<user>[0-9]+)/favorite/audio$',FavoriteAudio.as_view()),
    
    url(r'^message/$', ShowMessage.as_view()),
    url(r'^message/?P<user>[0-9]+$', ShowUserMessage.as_view()),
    url(r'^message/send$', CreateMessage.as_view()),
    url(r'^message/delete/?P<message_id>[0-9]+$', DeleteMessage.as_view()),
    url(r'^message/delete/?P<user>[0-9]+/all$', DeleteBulkMessage.as_view()),
    url(r'^message/delete/?P<user>[0-9]+/bulk$', DeleteAllMessage.as_view()),

    url(r'^post/add$', CreatePost.as_view(), name='add-post'),
    url(r'^post/update/?P<post_id>[0-9]+$', UpdatePost.as_view()),
    url(r'^post/delete/?P<post_id>[0-9]+$', DeletePost.as_view()),
    url(r'^post/?P<post_id>[0-9]+$', ShowPost.as_view()),
    url(r'^post/(?P<post_id>[0-9]+)/comments$', PostComments.as_view(),name='comment-on-post'),
    url(r'^post/(?P<post_id>[0-9]+)/share$', SharePost.as_view(), name='share-post'),
    
    url(r'^comment/add$', CreateComment.as_view(), name='add-comment'),
    url(r'^comment/update/(?P<comment_id>[0-9]+)$', UpdateComment.as_view(), name='update-comment'),
    url(r'^comment/delete/(?P<comment_id>[0-9]+)$', DeleteComment.as_view(), name='delete-comment'),
    
    url(r'^setting$', Settings.as_view()),
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)
