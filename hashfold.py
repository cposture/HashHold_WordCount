import sys
import re

class  HashFold(object):
	def  start(self,inputs):
		hash={}
		for input in inputs:
			f = self.map(input)
			for k,v in f:
				if k in hash:
					hash[k] = self.fold(hash[k],v)
				else:
					hash[k] = v
		return hash

class  WordCount(HashFold):
	STOP_WORDS = ('a','an','')
	def map(self,document):
		with  open(document,'r') as f:
			for line in f:
				for word in re.findall(r'\b[A-Za-z_][0-9A-Za-z_]*',line):
					if word.lower()  not in self.STOP_WORDS:
						yield word.strip(), 1

	def fold(self,count1, count2):
		return count1+count2
hash = WordCount().start(sys.argv)
for k in sorted(hash):
	print(k+'::'+str(hash[k]))