import webapp2
from urlparse import urlparse, urlunparse

class RedirectAction(webapp2.RequestHandler):
    def get(self):
        scheme, netloc, path, params, query, fragment = urlparse(self.request.url)

        if not "www" in netloc:
            netloc = "www." + netloc

        self.redirect(urlunparse((scheme, netloc, path, params, query, fragment)))


app = webapp2.WSGIApplication([
    ('/', RedirectAction),
], debug=False)