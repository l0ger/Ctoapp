from wsgiref.simple_server import make_server
import json
from Storage.Parse import Parse
from Crypto.crypto import crypto


def application(environ, start_response):
    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    # for invalid request
    if (request_body == "") or (request_body is None) or (request_body_size == 0):
        start_response('200 OK', ('Content-Type', 'text/plain'))
        return ""

    # for valid request
    d = json.loads(request_body)
    cypher = crypto()
    # use 24 byte key
    key = "FX0FGHC2QR59VDX4WE8SVFGK"
    d_encrypt = cypher.triple_des_encrypt(request_body, key)
    parse = Parse()
    print parse.upload(d_encrypt)
    response_body = unicode.encode(d.get('ip'))

    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response('200 OK', headers)
    return response_body

#httpd = make_server('localhost', 8000, application)
#print "Serving on port 8000..."
#httpd.serve_forever()
