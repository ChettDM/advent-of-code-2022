import os

from enum import Enum

data = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
lines = data.readlines()

opponentsMoves = []
requiredResult = []

# create moves lists
for line in lines:
    moves = line.strip().split(" ")
    opponentsMoves.append(moves[0])
    requiredResult.append(moves[1])


class RockPaperScissorsPlay(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


def convertSelectionToRockPaperScissorsPlay(selection):
    switch = {
        'A': RockPaperScissorsPlay.Rock,
        'B': RockPaperScissorsPlay.Paper,
        'C': RockPaperScissorsPlay.Scissors,
        'X': RockPaperScissorsPlay.Rock,
        'Y': RockPaperScissorsPlay.Paper,
        'Z': RockPaperScissorsPlay.Scissors,
    }
    return switch.get(selection)


def scoreRound(opponentsChoice, yourChoice):
    # 'A':'X':1,  # rock
    # 'B':'Y':2,  # paper
    # 'C':'Z':3,  # scissors

    # 0 if you lost, 3 if the round was a draw, and 6 if you won

    if convertSelectionToRockPaperScissorsPlay(opponentsChoice) == yourChoice:
        # draw
        return 3 + yourChoice.value
    if convertSelectionToRockPaperScissorsPlay(opponentsChoice) == RockPaperScissorsPlay.Rock and yourChoice == RockPaperScissorsPlay.Paper:
        # win
        return 6 + yourChoice.value
    if convertSelectionToRockPaperScissorsPlay(opponentsChoice) == RockPaperScissorsPlay.Paper and yourChoice == RockPaperScissorsPlay.Scissors:
        # win
        return 6 + yourChoice.value
    if convertSelectionToRockPaperScissorsPlay(opponentsChoice) == RockPaperScissorsPlay.Scissors and yourChoice == RockPaperScissorsPlay.Rock:
        # win
        return 6 + yourChoice.value
    # loss
    return 0 + yourChoice.value


winningSelection = {
    'A': RockPaperScissorsPlay.Paper,
    'B': RockPaperScissorsPlay.Scissors,
    'C': RockPaperScissorsPlay.Rock,
}

losingSelection = {
    'A': RockPaperScissorsPlay.Scissors,
    'B': RockPaperScissorsPlay.Rock,
    'C': RockPaperScissorsPlay.Paper,
}

score = 0
for i in range(len(lines)):
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

    if requiredResult[i] == 'X':  # lose
        currentRound = scoreRound(
            opponentsMoves[i], losingSelection.get(opponentsMoves[i]))
    elif requiredResult[i] == 'Y':  # draw
        currentRound = scoreRound(
            opponentsMoves[i], convertSelectionToRockPaperScissorsPlay(opponentsMoves[i]))
    else:  # win
        currentRound = scoreRound(
            opponentsMoves[i], winningSelection.get(opponentsMoves[i]))

    score += currentRound

print(score)
