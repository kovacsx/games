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
printNumbers = True
printHeuristics = False

# default test program
testDecks = ["1" * 60,
			"1" * 30 + "0"  + "1" * 30,
			"11011",
			"1001"]

# "main loop"

def printDeck(program, totalIterations = 0):
	global printNumbers

	if printHeuristics:
		count1s = program.count('1')
		count0s = program.count('0')
		
		print(f"Program ({count0s:4} : {count1s:4} : {count1s - count0s:4} : {len(program):4})\t: {str(investigatorChar * totalIterations * drawInvestigator)} {program.replace('0', clueChar).replace('1', suspectChar) }{mastermindChar}")
	elif printNumbers == True:
		progNumber = int(program[::-1], 2)
		print(f"{progNumber:32} {str(investigatorChar * totalIterations * drawInvestigator)}{program.replace('0', clueChar).replace('1', suspectChar) }{mastermindChar}")
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
	global printNumbers

	if len(sys.argv) > 1:
		print(f"User game!")

		if(sys.argv[1].isalnum()):
			progNum = int(sys.argv[1])
			game = bin(progNum)[2:][::-1]
			print(f"{sys.argv[1]} -> {game}")
			printNumbers = True
		else:
			game = sys.argv[1].replace('+', '1').replace('-', '0')

		printDeck(game, 0)
		GameOfInvestigatorAndTheMastermind(game)
		print()

	else:
		for game in testDecks:
			print(f"\n\n\nNew game:\n\n" )
			printDeck(game, 1)
			GameOfInvestigatorAndTheMastermind(game)
	return 0


if __name__ == '__main__':
    main()


