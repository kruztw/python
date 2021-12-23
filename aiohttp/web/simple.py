from aiohttp import web


app = web.Application()

# method 1
'''
async def hello(request):
    return web.Response(text="Hello, world")
app.add_routes([web.get('/', hello)])
'''


# method 2
routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")

app.add_routes(routes)





web.run_app(app)
