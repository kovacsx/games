# by Janis Kovalevskis (janis.kovalevskis@gmail.com) (c) 2021
# all respective rights apply, use at your own risk.

# "01" = 2
# "0001" = 8
# "0101" = 10
# ...

# f(p) : (p << 1) if (p[0] == 0) else (p >> 1 + p + 1)

# while((p := f(p)) > 1);

def collatz(program):
	try:

		if(len(program) < 1):
			return program

		if(program[0] == '1'):
			p1 = '0' + program;
			p2 = addProg(p1, program)
			p3 = addProg(p2, "1")
			return p3
		elif(program[0] == '0'):
			return program[1:]

		raise Exception(f"Program contains invalid symbol: {program[0]}")

	except Exception as e:
		raise e

def addProg(p1, p2):
	# quick and dirty- convert sequences to numbers, for arithmetic + operation
	# must be reversed before and after (bit order in string vs bit order in sequence are different)
	n1 = int(p1[::-1], 2)
	n2 = int(p2[::-1], 2)

	ret = bin(n1+n2)[2:] # remove "0b" prefix
	ret = ret[::-1] 

	return ret

