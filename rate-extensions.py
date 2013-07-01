#from google.appengine.api import users
import webapp2
import json
import logging
from Rater import *
from RateStub import *

class MainPage(webapp2.RequestHandler):
    """As this application is not about a webpage
       only a simple message is shown on the main
       page."""
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Not a site!')
        logging.info('Text response sent successfully!')

class PostApi(webapp2.RequestHandler):
    """REapi takes JSON string from the Rate-Extension
       Chrome extension, checks the permissions and
       returns the status as JSON."""
    def post(self):
        # First the JSON string is converted to a list
        # of  ExtensionInfo objects Python can work with.
        jsonString = self.request.body
        logging.debug('Raw JSON string: ' + str(jsonString))

        extensions = []
        if jsonString is not "":
            loadedString = json.loads(jsonString)
            logging.debug('Loaded string: ' + str(loadedString))

            parsed = []
            for extension in loadedString:
                name = extension["name"]
                permissions = extension["permissions"]
                enabled = extension["enabled"]
                parsed.append(ExtensionInfo(name, permissions, enabled))

            # Next the list is sent to processing, where
            # the list of ExtensionInfo objects are turned
            # into ProcessedExtensionInfo.
            #processedExtensions = RateStub()
            processedExtensions = Rate(parsed)
            
            for e in processedExtensions:
                extensions.append({
                    "name":e.name
                    , "category":e.category
                    , "rank":e.rank
                    , "enabled":e.enabled
                })
                logging.debug('ProcessedExtensions: ' + e.toString())
            
        # Then the list is converted to a JSON string
        response = {}
        response["extensions"] = extensions
        jsonResponse = json.dumps(response)

        # And lastly the JSON string is sent back to the
        # requester.
        self.response.headers['Content-Type'] = "application/json"
        logging.debug('JSON Response: ' + jsonResponse)
        self.response.out.write(jsonResponse)
        logging.info('JSON response sent successfully!')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api/v1/post', PostApi),
], debug=True)