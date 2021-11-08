# Collatz conjecture / 3x + 1 "runner"
# by Janis Kovalevskis (janis.kovalevskis@gmail.com) (c) 2021
# all respective rights apply, use at your own risk.

testString = reversed("1000000000")

testProgram = [c for c in testString]

# f(p) : (p >> 1) if (p[0] == 0) else (p << 1 + p + 1)

def collatz(program):
	try:

		print(f"program: {program}")

		if(program[0] == '0'):
			return collatz(program[1:])
		elif(program[0] == '1'):
			#p1 = program.
			if(len(program) > 1):
				raise Exception(f"Unimplemented yet....")
			return program
			

		raise Exception(f"program contains invalid symbol: {program[0]}")

	except Exception as e:
		raise e


def solver(program):
	totalIterations = int(0)
	while(len(program) > 1):
		program = collatz(program)
		print(program)
		totalIterations = totalIterations + 1
		if(totalIterations > 10000):
			print(f"Too many iterations!!!")
			break

	print(f"Total iterations: {totalIterations}")
	return True

def main():
	print(f"Test program: {testProgram}")
	solver(testProgram)
	return 0


if __name__ == '__main__':
    main()


