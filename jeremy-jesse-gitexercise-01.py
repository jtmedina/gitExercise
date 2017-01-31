# git-exercise-01.py

# TEAM LEADER:
# implement this function so that it returns copy of string_arg reversed
def reverseWord(string_arg):
	string_arg = list(string_arg)
	string_arg.reverse()
	return ''.join(string_arg)

# TEAM MEMBER:
# implement this function so that it returns the frequency of query in string_arg
def countFreq(string_arg, query):
	count = 0
	for i in string_arg:
		if i == query:
			count += 1
	return count

def main():
	data = 'guidorossumwashere'
	print 'REVERSED ==>', reverseWord(data)
	print 'FREQUENCY OF s IN', data, '==>', countFreq(data, 's')

if __name__ == "__main__": 
	main()