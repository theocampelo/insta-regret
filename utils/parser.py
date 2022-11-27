#!/usr/bin/python3

import os
import sys
import argparse

parser = argparse.ArgumentParser(
		prog = 'instantregret.py',
		usage='%(prog)s [options]',
		description = 'General instagram shell interaction'
	)

# login
parser.add_argument(
	'-l',
	action='store_true',		# Não leva nenhum argumento, e nargs precisa ser != 0
	help='Iniciar sessão autenticada no instagram'
	)

# single_comment
parser.add_argument(
	'-c',
	metavar=('<link do post>','<comentário>'),
	nargs=2,
	type=str,
	help='Comenta na publicação selecionada'
	)

# get_followers
parser.add_argument(
	'-f',
	action='store_true',
	help='Retorna a lista de seguidores do usuário logado'
	)

args = parser.parse_args()

if len(sys.argv) < 2:
	parser.print_usage()
	sys.exit(1)