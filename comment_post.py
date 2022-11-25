#!/usr/bin/python3
import login_instagram

#https://www.instagram.com/api/v1/web/comments/2952749785640743088/add/

class InstagramPost:
	def __init__(self):
		self.session = None

	def comment(session, text, post_url, add_url):
		s = session
		payload = {
			'comment_text':text
		}

		url = add_url
		r = s.get(url)

		# debug
		#print(s.headers, s.cookies.get_dict(), r.status_code)

		csrf = s.cookies['csrftoken']
		r = s.post(url, data=payload, headers={
			"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
	        "x-requested-with": "XMLHttpRequest",
	        "referer": post_url,
	        "x-csrftoken":csrf
		})


