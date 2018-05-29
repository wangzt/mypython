#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 @Author: tomsky.wang 
  @Date: 2018-05-29 17:54:03 
'''

import asyncio
import orm
from models import User


async def main(loop):
    await orm.create_pool(loop, **database)
    user = User()
    # user.id = 1
    user.name = 'tomsky.wang'
    user.passwd = '1234567890'
    user.email = 'tomsky.wang@gmail.com'
    user.admin = True
    user.image = 'about:blank'
    await user.save()
    await orm.destroy_pool()
    return user.name


loop = asyncio.get_event_loop()
database = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'db': 'py_test'
}

task = asyncio.ensure_future(main(loop))

res = loop.run_until_complete(task)

print(res)
print('\n===================')
loop.close()
