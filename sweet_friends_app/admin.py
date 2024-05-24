from django.contrib import admin

from .models import User, Friends

@admin.register(User)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','email','full_name']
    list_filter = ['id','email','full_name']


@admin.register(Friends)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_id','friend_id','is_hidden','status']
    list_filter = ['user_id','friend_id','is_hidden','status']
# admin.site.register(User)
# Register your models here.
