from collections import Counter
import requests

if __name__ == '__main__':
	try:
		keywords = requests.get('https://raw.githubusercontent.com/exorde-labs/TestnetProtocol/main/targets/keywords.txt')
	except:
		print('Error while fetching the file')
		exit()
	words = keywords.content.decode('utf-8')
	
	cleaned = list(set(words.replace(', ', '\n').replace(',', '\n').split('\n')))
	cleaned.remove('')
	cleaned.sort()
	print(len(cleaned), 'elements in total')
	print("Alpha order : ", cleaned)
	print('')
	print('Number of elements that have more that 4 characters:', len([e for e in cleaned if len(e) >= 4]))
	
	print('')
	raw_list = words.replace(', ', '\n').replace(',', '\n').split('\n')
	uniqued = False
	for word in cleaned:
		count = len([w for w in raw_list if w == word])
		if count == 1:
			uniqued = True
	if not uniqued:
		print('Le nombre de keyword unique est nul')
	else:
		print('Le nombre de keyword unique n\'est pas nul')
