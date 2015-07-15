from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User, City, Profile
# Register your models here.

class MyUserAdmin(UserAdmin):
    UserAdmin.add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2','first_name'),
        }),
    )
    list_display = ('username','email','id','first_name','last_name','is_staff')
    search_fields = ('first_name', 'last_name', 'email','username')
    ordering = ('username',)

    UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'email','password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','profile_photo','cover_image')}),
        ('advance_info',{'fields':('confirmation_code',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Subsriptions', {'fields': ('followers',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User,MyUserAdmin)
admin.site.register(City)
admin.site.register(Profile)