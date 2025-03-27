# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2025-03-27 12:25:13
# @Last Modified by:   Your name
# @Last Modified time: 2025-03-27 14:14:11

from sanic import Sanic
from sanic.response import json,text
import os

app = Sanic("vercel-api-gnpng")

@app.route('/')
async def index(request):
    return text(f'info: {os.cpu_count()}')

if __name__ == '__main__':
    app.run()
