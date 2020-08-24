from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id",)


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
