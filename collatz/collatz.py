# Collatz conjecture / 3x + 1 "runner"
# by Janis Kovalevskis (janis.kovalevskis@gmail.com) (c) 2021
# all respective rights apply, use at your own risk.

testProgram = "101010101001010101010"

def collatz(program):
	return program


def solver(program):
	totalIterations = 0
	while(len(progam) > 1):
		program = collatz(program)
		print program
		totalIterations++

	print(f"Total iterations: {totalIterations}")
	return True

def main():
	solver(testProgram)
	return 0


if __name__ == '__main__':
    main()


