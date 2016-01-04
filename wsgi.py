from wsgiref.simple_server import make_server
from cgi import escape, urlparse
import json


def application(environ, start_response):
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    request_body = environ['wsgi.input'].read(request_body_size)
    d = json.loads(request_body)
    response_body = unicode.encode(d.get('ip'))

    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response('200 OK', headers)
    return response_body

# httpd = make_server('localhost', 8000, application)
# print "Serving on port 8000..."
# httpd.serve_forever()
