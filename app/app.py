import sys
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from routes import homepage, findrecipe
from middleware import middleware


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/findrecipe', findrecipe, methods=["GET", "POST"])
] , middleware=middleware)

app.mount(
    '/static', StaticFiles(directory='./static/'))

if __name__ == '__main__':
    if 'serve' in sys.argv:
        uvicorn.run(app=app, host='0.0.0.0', port=5000, log_level="info")
