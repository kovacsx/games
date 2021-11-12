# by Janis Kovalevskis (janis.kovalevskis@gmail.com) (c) 2021
# all respective rights apply, use at your own risk.

# Game of Investigator and The Mastermind

import time
from collatz import collatz

drawInvestigator = 1

investigatorChar = 'I'
clueChar = '-'
suspectChar = '+'
mastermindChar = 'M'

# Developer settings

slowMode = False
printHeuristics = False

# default test program
testDecks = ["1" + "1" * 50  + "1" * 50 + "1",
			"1" + "1" * 50 + "0"  + "1" * 50 + "1",
			"1001",
			"101",
			]

# "main loop"

def GameOfInvestigatorAndTheMastermind(program):
	
	totalIterations = int(0)

	while(len(program) > 1):

		if printHeuristics:
			count1s = program.count('1')
			count0s = program.count('0')
			
			print(f"Program ({count0s:4} : {count1s:4} : {count1s - count0s:4} : {len(program):4})\t: {str(investigatorChar * totalIterations * drawInvestigator)} {program.replace('0', clueChar).replace('1', suspectChar) }{mastermindChar}")
		else:
			print(f"{str(investigatorChar * totalIterations * drawInvestigator)}{program.replace('0', clueChar).replace('1', suspectChar) }{mastermindChar}")

		program = collatz(program)

		totalIterations = totalIterations + 1


		if slowMode :
			time.sleep(1 / 20)

	print(f"Total iterations: {totalIterations}")
	return True

def main():

	for game in testDecks:
		GameOfInvestigatorAndTheMastermind(game)

	return 0


if __name__ == '__main__':
    main()


