#!/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import options, define

def main():
	tornado.options.parse_command_line()
