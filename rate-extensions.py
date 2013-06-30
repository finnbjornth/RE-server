#from google.appengine.api import users
import webapp2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Not a site!')

class REapi(webapp2.RequestHandler):
    """REapi takes JSON string from the Rate-Extension
       Chrome extension, checks the permissions and
       returns status."""
    def get(self):
        response = {}
        stuff = [{"enabled" : "true"}, {"category" : "Snoop"}, {"rank" : "Small Fry"}]
        response["Facebook Notifications"] = stuff
        print response

        self.response.headers['Content-Type'] = "application/json"
        self.response.out.write(json.dumps(response))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api/v1/', REapi),
], debug=True)