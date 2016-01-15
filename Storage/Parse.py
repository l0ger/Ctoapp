import urllib2
import json
import httplib

"""
  this class use parse.com cloud storage service to
  saving coming data from client.
"""


class Parse:
    def __init__(self):
        self.parse_app_id = "YJPtoPrJ8RZFD51fFE1PR545rlCVKOW6wJRs4guz"
        self.parse_rest_api_key = "ZDrk5Y7XkVW26xjvP1F1XBafTYxPapHvPn207KEX"

    def upload(self, data):
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('POST', '/1/files/info.txt', data, {
            "X-Parse-Application-Id": self.parse_app_id,
            "X-Parse-REST-API-Key": self.parse_rest_api_key,
            "Content-Type": "text/plain",
            'Content-Length': str(len(data))
        })
        result = json.loads(connection.getresponse().read())
        file_name = unicode.encode(result.get('name'))
        return self._assosicate_file(file_name)

    def _assosicate_file(self, file_name):
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        params = json.dumps({
            "name": "mehdi",
            "text": {
                "name": file_name,
                "__type": "File"
            }
        })

        headers = {
            "X-Parse-Application-Id": self.parse_app_id,
            "X-Parse-REST-API-Key": self.parse_rest_api_key,
            "Content-Type": "application/json"
        }

        connection.request('POST', '/1/classes/MyFile', params, headers),

        result = json.loads(connection.getresponse().read())
        return result
