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