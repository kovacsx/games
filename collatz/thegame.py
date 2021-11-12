# by Janis Kovalevskis (janis.kovalevskis@gmail.com) (c) 2021
# all respective rights apply, use at your own risk.

# Game of Investigator and The Mastermind

import sys
import time
from collatz import collatz

drawInvestigator = 1

investigatorChar = 'I'
clueChar = '-'
suspectChar = '+'
mastermindChar = 'M'

# Developer options

slowMode = False
printHeuristics = False

# default test program
testDecks = ["1" + "1" * 50  + "1" * 50 + "1",
			"1" + "1" * 50 + "0"  + "1" * 50 + "1",
			"1001",
			"101",
			"1"]

# "main loop"

def printDeck(program, totalIterations = 0):
		if printHeuristics:
			count1s = program.count('1')
			count0s = program.count('0')
			
			print(f"Program ({count0s:4} : {count1s:4} : {count1s - count0s:4} : {len(program):4})\t: {str(investigatorChar * totalIterations * drawInvestigator)} {program.replace('0', clueChar).replace('1', suspectChar) }{mastermindChar}")
		else:
			print(f"{str(investigatorChar * totalIterations * drawInvestigator)}{program.replace('0', clueChar).replace('1', suspectChar) }{mastermindChar}")


def GameOfInvestigatorAndTheMastermind(program):
	
	totalIterations = int(1)

	while(len(program) > 1):

		program = collatz(program)

		printDeck(program, totalIterations)

		totalIterations = totalIterations + 1

		if slowMode :
			time.sleep(1 / 20)

	print(f"Mastermind was captured in: {totalIterations} steps!\nCongratulations!")
	return True

def main():

	if len(sys.argv) > 1:
		print(f"User game!")
		game = sys.argv[1].replace('+', '1').replace('-', '0')
		printDeck(game, 0)
		GameOfInvestigatorAndTheMastermind(game)
		print()

	else:
		for game in testDecks:
			printDeck(game, 1)
			GameOfInvestigatorAndTheMastermind(game)
			print()

	return 0


if __name__ == '__main__':
    main()


