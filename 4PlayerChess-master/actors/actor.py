
class Actor():
  def __init__(self, strategy):
    self.strategy = strategy
  def make_move(self, board):
    return self.strategy.make_move(board)
