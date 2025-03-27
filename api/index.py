# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2025-03-27 12:25:13
# @Last Modified by:   Your name
# @Last Modified time: 2025-03-27 13:47:16

from sanic import Sanic
from sanic.response import json

app = Sanic("vercel-api-gnpng")

@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    return json({'hello': path})

if __name__ == '__main__':
    app.run()
