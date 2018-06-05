#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
  @Author: tomsky.wang
  @Date: 2018-06-03 11:11:47
'''

'url handlers'

import re
import time
import json
import logging
import hashlib
import base64
import asyncio

from coreweb import get, post
from models import User, Comment, Blog, next_id


@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }


@get('/api/users')
def api_get_users():
    users = yield from User.findAll(orderBy='create_at')
    for u in users:
        u.passwd = '******'
    return dict(users=users)
