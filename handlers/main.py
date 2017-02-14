from blog import *
from template import TemplateHandler

class MainHandler(TemplateHandler):
    """ MainHandler will redirect to main blog page """
    def get(self):
        self.redirect('/blog')
