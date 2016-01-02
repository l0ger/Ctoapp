def application(environ, start_response):

    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response('200 OK', headers)
    return environ['wsgi.input'].readline().decode()
