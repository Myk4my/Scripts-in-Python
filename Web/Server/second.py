def add(n1, n2):
	return n1+n2

def sub(n1, n2):
	return n1-n2

def mult(n1, n2):
	return n1*n2

def div(n1, n2):
	return n1/n2

def calc(cal, n1, n2):
	return cal(n1, n2)

result = calc(sub, 3, 4)
print(result)