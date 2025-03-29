from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Active user model reference
User = get_user_model()

# Extended user
class Extended_userInline(admin.StackedInline):
    model =ExtendedUser
    can_delete = False
    verbose_name_plural = 'ExtendedUsers' 

class CustomizedUserAdmin(UserAdmin):
    inlines = (Extended_userInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
# admin.site.register(Admin)

admin.site.register(Subject)
