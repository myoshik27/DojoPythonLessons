from urllib2 import urlopen

site_words = []
mySite = urlopen("http://dluxelife.com")
for oneLine in mySite:
	print oneLine
	lineWords = oneLine.split(' ')
	for word in lineWords:
		site_words.append(word.capitalize().replace('a','fuck',10).strip('\n'))
print site_words

counts = dict()
for words in site_words:
	if (counts.has_key(words) == False):
		counts[words] = 0
	counts[words] += 1

print counts


