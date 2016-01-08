import urllib2
import itertools
import mimetools
import mimetypes
from cStringIO import StringIO
import urllib


class Box:
    def __init__(self):
        self.developer_token = "ehButCog1MqR3AsH1TcjB7oWsjC3TXtO"
        self.folder_url = "https://api.box.com/2.0/folders"
        self.file_url = "https://api.box.com/2.0/files"
        self.upload_url = "https://upload.box.com/api/2.0/files"
        self.data_file_id = "48944801893"

    def upload_data(self, data):
        req = urllib2.Request(self.file_url + "/" + self.data_file_id)
        print self.upload_url + "/" + self.data_file_id + "/content"
        #req.get_method = lambda: 'GET'
        # req.add_data("sdsdsd")
        # req.add_data("sdsdd")

        # req.add_header('Accept', 'application/json')
        req.add_header('Content-type', 'text/html')
        req.add_header('Authorization', 'Bearer ' + self.developer_token)
        try:
            res = urllib2.urlopen(req)

            res.getcode()
            #print res.read()
            return res.read()

        except (urllib2.HTTPError, urllib2.URLError) as e:
            if hasattr(e, 'code'):
                e.code
                return e.code
            else:
                return e

    def download_data(self):
        pass
