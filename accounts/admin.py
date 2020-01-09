# -*- coding:utf-8 -*-

from django.contrib.auth.admin import UserAdmin
from accounts.forms import BlogUserChangeForm, BlogUserCreationForm

# Register your models here.
'''管理模板'''


class BlogUserAdmin(UserAdmin):
    form = BlogUserChangeForm
    add_form = BlogUserCreationForm
    list_display = ('id', 'nickname', 'username', 'email', 'last_login', 'date_joined', 'source')
    list_display_links = ('id', 'username')
    ordering = ('-id',)
