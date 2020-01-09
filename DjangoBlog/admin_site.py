# -*- coding:utf-8 -*-


from django.contrib.admin import AdminSite
from django.contrib.sites.admin import SiteAdmin
from django.contrib.admin.models import LogEntry
from django.contrib.sites.models import Site
from DjangoBlog.logentryadmin import LogEntryAdmin
from accounts.models import BlogUser
from blog.admin import *
from accounts.admin import *
from blog.models import Category, Tag, Links, SideBar, BlogSettings
from comments.models import Comment
from oauth.admin import *
from oauth.models import OAuthUser, OAuthConfig
from servermanager.admin import *
from comments.admin import *
from owntracks.admin import *
from servermanager.models import commands, EmailSendLog


class DjangoBlogAdminSite(AdminSite):
    site_header = 'DjangoBlog administration'
    site_title = 'DjangoBlog site admin'

    def __init__(self, name='heihei'):
        super().__init__(name)

    def has_permission(self, request):
        return request.user.is_superuser

    # def get_urls(self):
    #     urls = super().get_urls()
    #     from django.urls import path
    #     from blog.views import refresh_memcache
    #
    #     my_urls = [
    #         path('refresh/', self.admin_view(refresh_memcache), name="refresh"),
    #     ]
    #     return urls + my_urls


admin_site = DjangoBlogAdminSite(name='heihei')

admin_site.register(Article, ArticlelAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Tag, TagAdmin)
admin_site.register(Links, LinksAdmin)
admin_site.register(SideBar, SideBarAdmin)
admin_site.register(BlogSettings, BlogSettingsAdmin)

admin_site.register(commands, CommandsAdmin)
admin_site.register(EmailSendLog, EmailSendLogAdmin)

admin_site.register(BlogUser, BlogUserAdmin)

admin_site.register(Comment, CommentAdmin)

admin_site.register(OAuthUser, OAuthUserAdmin)
admin_site.register(OAuthConfig, OAuthConfigAdmin)

admin_site.register(OwnTrackLog, OwnTrackLogsAdmin)

admin_site.register(Site, SiteAdmin)

admin_site.register(LogEntry, LogEntryAdmin)
