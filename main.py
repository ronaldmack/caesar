#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt
import cgi


form="""
<html>
    <head>
        <title>Caesar</title>
    </head>

    <body>
        <form method="post">
            <label for="rotation">Rotate by:</label> <input type="text" name="rotation" value="0" size="5" class="" /><br/>
            <textarea name="text" style="height: 100px; width: 400px;">%(entry)s</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def write_form(self, entry="",rotation=""):
        self.response.out.write(form %{"entry": entry})

    def get(self):
        self.write_form()

    def post(self):
        e = self.request.get('text')
        r = int(self.request.get('rotation'))
        f = encrypt(e,r)
        self.write_form(f)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
