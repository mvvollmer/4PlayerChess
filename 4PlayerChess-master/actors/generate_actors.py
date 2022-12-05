import sys
sys.path.append('./4PlayerChess-master/')
from actors.actor import Actor
from actors.randomStrategy import RandomStrategy
from actors.minimaxStrategy import MinimaxStrategy
from actors.evaluation import Evaluation, EvaluationV2
from actors.moveOrdering import GlobalHistoryHeuristic, TranspositionTable

player_colors = ['r', 'b', 'y', 'g']

# Str --> Strategy:
# random: RandomStrategy
# minimax: minimaxStrategy
# none: Normal Player

# File for converting input string into Actor class objects
def generate_actors(input_strings):
  '''
  Parameters:
   - input_strings: an array of input strings
  '''
  players = []
  player_strings = input_strings[1:]
  globalHistory = GlobalHistoryHeuristic(12)
  globalTT = TranspositionTable()
  for i, player in enumerate(player_strings):
    if player == 'random':
      rStrat = RandomStrategy(player_colors[i])
      actor = Actor(rStrat)
      players.append((player_colors[i], actor))
    elif player == 'minimax':
      mStrat = MinimaxStrategy(player_colors[i], 4, Evaluation(), globalHistory, globalTT)
      actor = Actor(mStrat)
      players.append((player_colors[i], actor))
    elif player == 'minimax2':
      mStrat = MinimaxStrategy(player_colors[i], 4, EvaluationV2(), globalHistory, globalTT)
      actor = Actor(mStrat)
      players.append((player_colors[i], actor))
  
  return players
  