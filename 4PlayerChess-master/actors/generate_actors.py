import sys
sys.path.append('./4PlayerChess-master/')
from actors.actor import Actor
from actors.randomStrategy import RandomStrategy

player_colors = ['r', 'b', 'y', 'g']

# Str --> Strategy:
# random: RandomStrategy
# none: Normal Player

# File for converting input string into Actor class objects
def generate_actors(input_strings):
  '''
  Parameters:
   - input_strings: an array of input strings
  '''
  players = []
  player_strings = input_strings[1:]
  for i, player in enumerate(player_strings):
    if player == 'random':
      rStrat = RandomStrategy(player_colors[i])
      actor = Actor(rStrat)
      players.append((player_colors[i], actor))
  
  return players
  