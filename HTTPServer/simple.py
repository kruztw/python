#!/usr/bin/env python3


from http.server import HTTPServer, BaseHTTPRequestHandler

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', 8888)
       self.end_headers()


HTTPServer(("", 6666), Redirect).serve_forever()
