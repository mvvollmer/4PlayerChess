import sys

sys.path.append('./4PlayerChess-master/')
from strategy import Strategy
from gui.board import Board


class RandomStrategy(Strategy):
  def __init__(self, player):
    super().__init__(player)
  def make_move(board: Board):
    board.printBB256()
