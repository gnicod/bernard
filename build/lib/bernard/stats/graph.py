# coding: utf-8
from aiohttp.web_request import Request
from aiohttp.web_response import json_response, Response

async def draw_graph(request: Request):

    verify_token = request.query.get('hub.verify_token')

    if not verify_token:
        return json_response({
            'error': 'No verification token was provided',
        }, status=400)

    return json_response({
        'error': 'could not find the page token in configuration.'
    })
