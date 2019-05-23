from dict import LETTERS

from unicodedata import normalize

def remove_special_characters(text):
	"""=========================================================================
	Método para remover caracteres especiais do texto.
	========================================================================="""
	return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

def count_holes(text):
	"""=========================================================================
	Método conta numero de buracos.
	========================================================================="""
	count = 0
	# removo caracteres especiais
	text = remove_special_characters(text)
	# para cada letra busco no dict o numero de buracos
	for i in text:
		# e adciono em count
		count += LETTERS[i]
	return count
