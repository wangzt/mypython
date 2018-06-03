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
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }

