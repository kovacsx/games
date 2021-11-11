from collatz import collatz

drawInvestigator = 1

# testProgram = "0" * 20 + "1" * 20 + "0" * 20 + "1" * 20
# testProgram = "1" * 1000
# testProgram = "1" * 100 + "110000111100111101001111110111100111110010000111100100000101010111011000011100100100100101010110010000110111100101101110111001001001110001101110010011101010001010010001100101011011001001001001111010111001010101000000100101011001001001110011000111011001110001100001001101111111100010001110001001100100100010101111010001010011011111101011010011011101001101011000100001101001100010011100110111101001111000010101000100101111011010000010010110001001100010110110001101111101011100101000011010010000101011001100110110000011100111100100"
# testProgram = "1" * 20 + "010101010101" + "1" * 20
testProgram = "1" + "1" * 100  + "1" * 40 + "1"
# testProgram = "".join(['0' if r % 2 == 0 else '1' for r in range(1,20)])
# testProgram = testString[::-1] # reverse bit order


def solver(program):
	totalIterations = int(0)
	while(len(program) > 1):
		count1s = program.count('1')
		count0s = program.count('0')
		print(f"Program ({count0s:4} : {count1s:4} : {count1s - count0s:4} : {len(program):4})\t: {str('*' * totalIterations * drawInvestigator)} {program}")

		program = collatz(program)

		totalIterations = totalIterations + 1

		if totalIterations > 20000:
			break

		# time.sleep(1 / 20)

	print(f"Total iterations: {totalIterations}")
	return True

def main():
	print(f"Test program: {testProgram}")
	solver(testProgram)
	return 0


if __name__ == '__main__':
    main()


