import re, requests
from datetime import datetime
from getpass import getpass

class LoginPage:
	def __init__(self):
		self.session = None
	
	def authenticate():
		
		# Login no instagram
		print('[LOGIN]')
		username = input('Username: ')
		password = getpass()

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
			#print(s.headers, s.cookies.get_dict(), r.status_code)

			csrf = s.cookies['csrftoken']
			r = s.post(login_url, data=payload, headers={
				"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
		        "x-requested-with": "XMLHttpRequest",
		        "referer": "https://www.instagram.com/accounts/login/",
		        "x-csrftoken":csrf
				})

		#print(r.text)
		# Retorna a sessão logada
		return s