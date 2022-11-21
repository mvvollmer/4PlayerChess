import sys
import random
from collections import deque

sys.path.append('./4PlayerChess-master/')
from gui.board import Board
from actors.strategy import Strategy
from actors.moveOrdering import mvv_lva, KillerMoves
from actors.evaluation import Evaluation



class MinimaxStrategy(Strategy):
    # self.eval = evaluation()
    def __init__(self, player, maxDepth):
        super().__init__(player)
        self.maxDepth = maxDepth
        self.killerMoves = KillerMoves(maxDepth)
        self.evaluation = Evaluation()
        self.nextColor = deque(['r', 'b', 'y', 'g'])
        while self.nextColor[0] != self.player:
          self.nextColor.rotate(-1)

    def negamax(self, color: str, board: Board, depth: int, alpha: float = float("-inf"), beta: float = float("inf")):
        colorNum = board.colorMapping[color]
        if board.checkMate(colorNum) or depth >= self.maxDepth:
            return self.evaluation.evaluateBoard(colorNum, board), None
        moves, captures = self.getAllLegalMoves(color, board)
        orderedCaptures = mvv_lva(captures, board)
        orderedMoves = self.killerMoves.sortMoves(moves, depth)
        actions = orderedCaptures + orderedMoves
        maxEval = float("-inf")
        bestAction = None
        for action in actions:
            nextBoardState = self.getNewBoard(board, *action)
            self.nextColor.rotate(-1) # this code might not work
            eval, _ = self.negamax(self.nextColor[0], nextBoardState, depth + 1, -beta, -alpha)
            eval = -eval
            self.nextColor.rotate(1)
            # TODO: Add killer move heuristic
            if eval > maxEval:
              maxEval = eval
              bestAction = action
              alpha = max(alpha, eval)
              if beta <= alpha:
                  # pretty sure killer move is added here
                  return maxEval, bestAction
        return maxEval, bestAction

    def make_move(self, board: Board):
        _, action = self.negamax(self.nextColor[0], board, 0)
        return action

