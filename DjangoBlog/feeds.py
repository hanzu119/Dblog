# -*- coding: utf-8 -*-


from django.contrib.syndication.views import Feed
from blog.models import Article
from django.utils.feedgenerator import Rss201rev2Feed
from DjangoBlog.utils import CommonMarkdown
from django.contrib.auth import get_user_model
from datetime import datetime


def author_name():
    if get_user_model().objects.first():
        return get_user_model().objects.first().nickname


def author_link():
    return get_user_model().objects.first().get_absolute_url()


def items():
    return Article.objects.order_by('-pk')[:5]


def feed_copyright():
    now = datetime.now()
    return "Copyright© {year} agpg".format(year=now.year)


class DjangoBlogFeed(Feed):
    feed_type = Rss201rev2Feed

    description = '学而不思则罔，思而不学则怠.'
    title = "学而不思则罔，思而不学则怠. "
    link = "/feed/"

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return CommonMarkdown.get_markdown(item.body)

    def item_link(self, item):
        return item.get_absolute_url()

    def item_guid(self, item):
        return
