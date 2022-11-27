#!/usr/bin/python3

import sys
from os.path import exists
import time, re, requests as r
from getpass import getpass
from bs4 import BeautifulSoup

from utils import auth as a
from utils import post as p
from utils import parser
from utils import debug

args = parser.args

def login():
	print('[LOGIN]')
	username = input('Username: ')
	password = getpass()
	s = a.Session.authenticate(username, password)

	return s

def single_comment():
	if not exists("tokens/current.session"):
		print("* sessão não logada, faça o login para continuar.\n")
		s = login()
	else:
		print("* resumindo sessão de login...\n")
		s = a.Session.load_cookies()

	print('[POSTAR COMENTÁRIO]')
	post_url = args.c[0]
	comment  = args.c[1]

	print(f"* postando comentário: {comment}")
	p.Post.comment(s, comment, post_url)

METHOD_MAP = {
	'l':login,
	'c':single_comment
}

arg_values = list(vars(args).values())

if arg_values[0] == True:
	METHOD_MAP['l']()
else:
	for i, value in enumerate(arg_values):
		if value != (None or False):
			list(METHOD_MAP.values())[i]()