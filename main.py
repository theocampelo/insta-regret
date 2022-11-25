#!/usr/bin/python3

import time, re
from bs4 import BeautifulSoup
import login_instagram as li
import comment_post as cp
import get_post_id as gi

#import debug_requests

# Filtragem do arquivo CSV
filename = "followers.csv"
#filename = "test.csv"
f = open(filename, 'r')
followers = list()

# Adiciona os seguidores do CSV na lista
for line in f: followers.append(re.split(',|\n', str(line))[1])

# GET Sessão autenticada
s = li.LoginPage.authenticate()
post_url = "https://www.instagram.com/p/ClW5xc6O95Q/"

# Pega o ID do post
add_url = "https://www.instagram.com/api/v1/web/comments/" + gi.Post.get_id(s, post_url) + "/add/"

# Comenta, em loop, a lista de usuários
for arroba in followers:
	comment = arroba
	print(f"* marcando {arroba}")
	cp.InstagramPost.comment(s, comment, post_url, add_url)

	time.sleep(10)