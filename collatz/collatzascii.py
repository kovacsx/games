from collatz import collatz

drawInvestigator = 1

investigatorChar = 'I'
clueChar = '-'
suspectChar = '+'
mastermindChar = 'M'


# default test program
testDecks = ["1" + "1" * 50  + "1" * 50 + "1", \
			"1" + "1" * 50 + "0"  + "1" * 50 + "1"]

printHeuristics = False

# testProgram = "".join(['0' if r % 2 == 0 else '1' for r in range(1,20)])
# testProgram = testString[::-1] # reverse bit order


def GameOfInvestigatorAndTheMastermind(program):
	totalIterations = int(0)
	while(len(program) > 1):
		count1s = program.count('1')
		count0s = program.count('0')

		if printHeuristics:
			print(f"Program ({count0s:4} : {count1s:4} : {count1s - count0s:4} : {len(program):4})\t: {str(investigatorChar * totalIterations * drawInvestigator)} {program.replace('0', clueChar).replace('1', suspectChar) }{mastermindChar}")
		else:
			print(f"{str(investigatorChar * totalIterations * drawInvestigator)}{program.replace('0', clueChar).replace('1', suspectChar) }{mastermindChar}")

		program = collatz(program)

		totalIterations = totalIterations + 1

		if totalIterations > 20000:
			break

		# time.sleep(1 / 20)

	print(f"Total iterations: {totalIterations}")
	return True

def main():

	for game in testDecks:
		GameOfInvestigatorAndTheMastermind(game)

	return 0


if __name__ == '__main__':
    main()


