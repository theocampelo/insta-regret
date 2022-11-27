import re, requests, os, pickle
from datetime import datetime
from getpass import getpass

class Session:
	def __init__(self):
		self.session = None

	def load_cookies():
		s = requests.Session()
		# insert cookies to cookie jar of new session
		with open('tokens/current.session', 'rb') as f:
		    s.cookies.update(pickle.load(f))

		return s

	def authenticate(username, password):
		time = int(datetime.now().timestamp())

		payload = {
			'username':username,
			'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
			'queryParams':{},
			'optIntoOneTap':'false'
		}
	
		link = 'https://instagram.com/accounts/login/'
		login_url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'

		with requests.Session() as s:
			r = s.get(login_url)
			print(s.headers, s.cookies.get_dict(), r.status_code)
			
			csrf = s.cookies['csrftoken']

			# f = open("tokens/csrf.token", "w")
			# f.write(csrf)
			# f.close()

			with open('tokens/current.session', 'wb') as f:
				pickle.dump(s.cookies, f)

			r = s.post(login_url, data=payload, headers={
				"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
		        "x-requested-with": "XMLHttpRequest",
		        "referer": "https://www.instagram.com/accounts/login/",
		        "x-csrftoken":csrf
				})

		print("\nsession: r.text -> " + r.text)
		# Retorna a sessão logada

		return s