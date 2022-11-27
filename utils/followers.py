import requests

class Followers:
	def __init__(self):
		self.session = None

	def get(session, user_id):
		s = session

		#payload = {
		#	https://www.instagram.com/api/v1/users/45070845411/info/
		#	'route_url':f'https://instagram.com/{username}/followers/'
		#}

		#ajax_url = 'https://www.instagram.com/ajax/navigation/'
		ajax_url = 'https://www.instagram.com/api/v1/friendships/{user_id}/followers/?count=12&search_surface=follow_list_page'
		#ajax_url = 'https://www.instagram.com/api/v1/users/45070845411/info/'
		r = s.get(ajax_url)

		followers_list = r.content

		return followers_list