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

#define("port", default=8000, help="run on the given port", type=int)
#$python server.py --port=port-num
define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="Personal", help="database name")
define("mysql_user", default="crmiv", help="database user")
define("mysql_password", default="ljn7168396", help="database password")

'''def handle_request(request):
	message = "hello,you request %s\n" % request.uri
	request.connection.write("HTTP1.1 200 OK\r\nContent-Length:%d\r\n\r\n%s" % (
		len(message),message))
	request.finish()
'''

class MainRequestHandler(tornado.web.RequestHandler):
	#render to index.html
	#Subclass RequestHandler,use get method
	#SUPPORTED_METHOD { }
    #attribute
	@property
    def db(self):
        return self.application.db
	def get_current_user(self,user):
		return self.get_secure_cookie(user)
	#def get():
		#pass parameter from self.render("xxx.html",***)
	#	self.render("index.html")
		#self.get_argument('','')   variable default-value	
	#def get_current_user(self):
	#	user_id = self.get_secure_cookie("user")
	#	if not user_id: return None

class RegisterHandler(MainRequestHandler):
	def post(self):
		Id = self.get_argument("CId",None)
		Password = self.get_argument("CPassword",None)
		Sex = self.get_argument("CSex",None)
		_temp = hash(Password)
		if Id is not None:
			if Password is not None:
				if Sex is not None:
					query_string_register = "SELECT * FROM user WHERE id=%s" % Id
					result_register = self.db.get(query_string_register)
					if result_register is None:
						self.db.




class AuthLogoutHandler(MainRequestHandler):
    def get(self):
        self.clear_cookie("user")
        #self.redirect(self.get_argument("next", "/"))

class AuthLoginHandler(MainRequestHandler):
	@tornado.web.asynchronous
	def get(self):
		Id = self.get_argument("CId",None)
		Password = self.get_argument("CPassword",None)
		query_string_login = "SELECT * FROM user WHERE id=%s" % Id
		result = self.db.get(query_string)
		_temp = hash(Password)
		if result['Password'] != _temp:
			#unsuccessful
			raise tornado.web.HTTPError(401)
		else:
			self.set_secure_cookie(Id,Id)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
				(r"/",MainHandler),
				(r"/register",RegisterHandler),
				(r"/login",AuthLoginHandler),
				(r"/logout",AuthLogoutHandler),
				]
		settings = dict(
			#picture file
			"static_path" : os.path.join(os.path.dirname(__file__), "static"),
			"template_path" : os.path.join(os.path.dirname(__file__), "templates"),
			"gzip" : True,
			"debug" : True,
			"login_url": "/login"，
			#ui_modules={"":};
			cookie_secret="bZJc2sWbQLKos6GkHn/VB9oX6GkHn/VB9oXwQt"
		)
		tornado.web.Application.__init__(self,handlers,**settings)
		self.db = torndb.Connection(
				host=options.mysql_host, database=options.mysql_database,
				user=options.mysql_user, password=options.mysql_password
		)

if __name__ == '__main__':
"""
	Command line formats are what you would expect (``--myoption=myvalue``).
Config files are just Python files. Global names become options, e.g.::
	
	config-file format: 
	config.py
		global_name = "value"
		name = "myname"
"""
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

