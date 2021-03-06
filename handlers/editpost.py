from google.appengine.ext import db
from blog import *
from models.users import Users
from models.blogs import Blogs
from template import TemplateHandler
from blog import BlogFunctions

class EditPostHandler(TemplateHandler, BlogFunctions):
    """ This is Class Handler for  editing of blog posts """
    
    def get(self, blog_id):
        """ uses get request to get editpost.html """
	self.check_user_redirect()
	blog = Blogs.blog_by_id(blog_id)
        self.blog_author_check(blog_id)

        self.render(
            'edit-post.html',
            blog=blog,
            delete_post='/blog/{blog_id}/delete'.format(blog_id=str(blog_id))
            )

    
    def post(self, blog_id):
        """handles the POST request from newpost.html"""
	self.check_user_redirect()
	blog = Blogs.blog_by_id(blog_id)
        self.blog_author_check(blog_id)

	title = self.request.get('subject')
        content = self.request.get('content')
	if title and content:
	    blog.edit(title, content)
            self.blog_redirect(blog_id)
        else:
             error = 'Need both title and content'
             self.render(
                 'edit-post.html',
                  blog={'title': '', 'content': ''},
                  blog_title=title,
                  blog_content=content,
                  error=error)


