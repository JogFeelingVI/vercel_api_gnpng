# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2025-03-27 12:25:13
# @Last Modified by:   Your name
# @Last Modified time: 2025-03-27 14:00:23

from sanic import Sanic
from sanic.response import json

app = Sanic("vercel-api-gnpng")

@app.route('/test')
async def test(request):
    return json({'info': 'hello world'})

if __name__ == '__main__':
    app.run()
