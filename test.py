#!/bin/env python

#support python 3.X
from __future__ import absolute_import, withj_statement

import os
import tornado
import torndb
import tornado.httpserver
import tornado.ioloop
from tornado import web
from tornado.options import define, options

define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="Personal", help="blog database name")
define("mysql_user", default="crmiv", help="blog database user")
define("mysql_password", default="ljn7168396", help="blog database password")

def handle_request(request):
	message = "hello,you request %s\n" % request.uri
	request.connection.write("HTTP1.1 200 OK\r\nContent-Length:%d\r\n\r\n%s" % (
		len(message),message))
	request.finish()

class MainRequestHandler(tornado.web.RequestHandler):
	#render to index.html
	#Subclass RequestHandler,use get method
	#SUPPORTED_METHOD { }
	def get():
		#pass parameter from self.render("xxx.html",***)
		self.render("index.html")
	
	def db(self):
		return self.application.db
	
	def get_current_user(self):
		user_id = self.get_secure_cookie("user")
		if not user_id: return None
		return self.db.get("SELECT * FROM authors WHERE id = %s", int(user_id))
	

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
				(r"/",MainHandler),
				]
		settings = dict(
			"static_path" : os.path.join(os.path.dirname(__file__), "static"),
			"template_path" : os.path.join(os.path.dirname(__file__), "templates"),
			"gzip" : True,
			"debug" : True,
			#ui_modules={"":};
			#cookie_secret="RANDOM_VALUE"
		)
		tornado.web.Application.__init__(self,handlers,**settings)

class AuthLogoutHandler()

class handleSql():
	def __init__(self):


if __name__ == '__main__':
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

