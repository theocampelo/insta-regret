import requests
from bs4 import BeautifulSoup

class Post:
	def __init__(self):
		self.session = None

	def get_id(session, post_url):
		s = session
		r = s.get(post_url)

		source_code = r.content
		soup = BeautifulSoup(source_code, features="html.parser")

		meta = soup.find("meta", property="al:ios:url")
		
		#print(meta["content"].split("instagram://media?id=")[1])

		post_id = meta["content"].split("instagram://media?id=")[1]

		return post_id

	def comment(session, text, post_url):
		s = session

		payload = {
			'comment_text':text
		}

		url = "https://www.instagram.com/api/v1/web/comments/" + Post.get_id(s, post_url) + "/add/"
		r = s.get(url)
		print(url)

		# debug
		#print(s.headers, s.cookies.get_dict(), r.status_code)

		csrf = s.cookies['csrftoken']
		r = s.post(url, data=payload, headers={
			"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
	        "x-requested-with": "XMLHttpRequest",
	        "referer": post_url,
	        "x-csrftoken":csrf
		})