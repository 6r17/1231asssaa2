import re
from collections import Counter
import requests
import json

if __name__ == '__main__':
	try:
		r = requests.get('https://bafybeidqw6oyclcnmqjbj2472vzofyhafdtot5woenazsgpmm3b6irnaoi.ipfs.w3s.link/')
	except:
		print('Error while fetching the file')
		exit()

	content = r.json()['Content']
	stringed = json.dumps(content, indent=2)

	print(len(content), 'elements in result request')
	print(len([entry for entry in content if 'http' in entry['Content']]), 'entries have a link in Content attribute')
	
	used_words = {}
	for entry in content:
		words = re.split(' |,|\n|\|', entry['Content']) # this requires a little bit more care
		for word in words:
			if (len(word) >= 8 and len(word) <= 20):
				if not used_words.get(word):
					used_words[word] = 1
				else:
					used_words[word] = used_words[word] + 1
	used_words = list(used_words.items())
	used_words.sort(key=lambda x:x[1])
	print(used_words[len(used_words) - 5:])
