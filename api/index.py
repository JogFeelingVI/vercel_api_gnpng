# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2025-03-27 12:25:13
# @Last Modified by:   Your name
# @Last Modified time: 2025-03-28 08:40:36

from sanic import Sanic
from sanic.request import Request
from sanic.response import text,json
import os

app = Sanic("vercel-api-gnpng")

@app.route('/')
async def index(request:Request):
    return text(f'你好,欢迎使用GNA.\nHello, welcome to GNA.\nこんにちは、GNAへようこそ.')

