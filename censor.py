def censor(text,word):
	return text.replace(word,"*" * len(word))
	
print censor("now is the time for all good men to come to the aid of their country","the")
