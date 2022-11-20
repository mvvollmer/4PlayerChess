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
        if board.checkMate(colorNum):
            return self.evaluation.evaluateBoard(colorNum, board), None
        moves, captures = self.getAllLegalMoves(color, board)
        orderedCaptures = mvv_lva(captures, board.boardData)

        orderedMoves = self.killerMoves.sortMoves(moves, depth)
        actions = orderedCaptures + orderedMoves

        if color == 'r' or color == 'y':
            maxEval = float("-inf")
            bestAction = None
            for action in actions:
                nextBoardState = self.getNewBoard(board, *action)
                self.nextColor.rotate(-1) # this code might not work
                eval = -self.negamax(self.nextColor[0], nextBoardState, depth + 1, -beta, -alpha)
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
        self.negamax(self.nextColor[0], board, 0)

