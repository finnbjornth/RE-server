#from google.appengine.api import users
import webapp2
import json

class MainPage(webapp2.RequestHandler):
    """As this application is not about a webpage
       only a simple message is shown on the main
       page."""
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Not a site!')

class PostApi(webapp2.RequestHandler):
    """REapi takes JSON string from the Rate-Extension
       Chrome extension, checks the permissions and
       returns the status as JSON."""
    def post(self):
        response = {}
        # Only a stub at the moment.
        extensions = [
             {"name":"Facebook notification","enabled":"true","category":"Snoop","rank":"Small Fry"}
             ,{"name":"Herpa Derpa","enabled":"true","category":"Snoop","rank":"Small Fry"}
             ,{"name":"Merpa skerf","enabled":"true","category":"Snoop","rank":"Small Fry"}
             ,{"name":"Skerfa smurfa","enabled":"true","category":"Snoop","rank":"Small Fry"}
        ]
        response["extensions"] = extensions

        self.response.headers['Content-Type'] = "application/json"
        self.response.out.write(json.dumps(response))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api/v1/post', PostApi),
], debug=True)