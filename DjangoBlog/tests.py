# -*- coding: utf-8 -*-

from django.test import TestCase
from DjangoBlog.utils import *


class DjangoBlogTest(TestCase):
    def setUp(self):
        pass

    def test_utils(self):
        md5 = get_md5('test')
        self.assertIsNotNone(md5)
        c = CommonMarkdown.get_markdown('''
        # Title1  
        
        ```python
        import os
        ```  
        
        [url](https://www.lylinux.net/)  
          
        [ddd](http://www.baidu.com)  
        
        
        ''')
        self.assertIsNotNone(c)
        d = {
            'd': 'key1',
            'd2': 'key2'
        }
        data = parse_dict_to_url(d)
        self.assertIsNotNone(data)
        render = BlogMarkDownRenderer()
        s = render.autolink('http://www.baidu.com')
        self.assertTrue(s.find('nofollow') > 0)
        s = render.link('http://www.baidu.com', 'test', 'test')
        self.assertTrue(s.find('nofollow') > 0)
