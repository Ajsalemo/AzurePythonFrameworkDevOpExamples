from bottle import route, default_app, run

@route('/')
def index():
    return 'Hello World, from Bottle - deployed with Azure DevOps pipelines'

# This can be used in development - Bottle uses WSGIRef in development mode
# run(app, host='localhost', port=8000)

# This can be used in production - for example, using Gunicorn to run against this instance of bottle
# Such as gunicorn app:app --bind='0.0.0.0:8000'
app = default_app()
