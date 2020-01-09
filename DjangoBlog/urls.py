# -*- coding: utf-8 -*-

from django.contrib.sitemaps.views import sitemap
from DjangoBlog.sitemap import StaticViewSitemap, ArticleSiteMap, CategorySiteMap, TagSiteMap, UserSiteMap
from DjangoBlog.feeds import DjangoBlogFeed
from django.conf import settings
from django.conf.urls.static import static
from DjangoBlog.admin_site import admin_site
from django.urls import include, re_path

sitemaps = {

    'blog': ArticleSiteMap,
    'Category': CategorySiteMap,
    'Tag': TagSiteMap,
    'User': UserSiteMap,
    'static': StaticViewSitemap
}

handler404 = 'blog.views.page_not_found_view'
handler500 = 'blog.views.server_error_view'
handle403 = 'blog.views.permission_denied_view'
urlpatterns = [
                  re_path(r'^heihei/', admin_site.urls),
                  re_path(r'', include('blog.urls', namespace='blog')),
                  re_path(r'mdeditor/', include('mdeditor.urls')),
                  re_path(r'', include('comments.urls', namespace='comment')),
                  re_path(r'', include('accounts.urls', namespace='account')),
                  re_path(r'', include('oauth.urls', namespace='oauth')),
                  re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                      name='django.contrib.sitemaps.views.sitemap'),
                  re_path(r'^search', include('haystack.urls'), name='search'),
                  re_path(r'', include('servermanager.urls', namespace='servermanager')),
                  re_path(r'', include('owntracks.urls', namespace='owntracks'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
