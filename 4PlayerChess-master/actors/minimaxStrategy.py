import sys
import random

sys.path.append('./4PlayerChess-master/')
from gui.board import Board
import actor
from actors.strategy import Strategy
from actors.moveOrdering import mvv_lva, KillerMoves



class Minimax(Strategy):
    # self.eval = evaluation()
    def __init__(self, actor, maxDepth):
        super().__init__(actor, "minimax")
        self.maxDepth = maxDepth
        self.killerMoves = KillerMoves()
        self.nextColor = ['r', 'b', 'y', 'g']
        while self.nextColor[0] != self.player:
          self.nextColor.rotate(-1)

    def minimax(self, color: actor, board: Board, depth: int, alpha: float = float("-inf"), beta: float = float("inf")):
        if board.checkMate(color):
            return evaluation(board), None

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
                eval = self.minimax(self.nextColor, nextBoardState, depth + 1, alpha, beta)
                self.nextColor.rotate(1)
                if eval > maxEval:
                  maxEval = eval
                  bestAction = action
                  alpha = max(alpha, eval)
                  if beta <= alpha:
                      return maxEval, bestAction
            return maxEval, bestAction
        else:
            minEval = float("inf")
            bestAction = None
            for square in board.getSquares():
                nextBoardState = self.getNewBoard(board, *action)
                self.nextColor.rotate(-1) # this code might not work
                eval = self.minimax(square, depth - 1, alpha, beta)
                self.nextColor.rotate(1)
                if eval < minEval: 
                  minEval = eval
                  bestAction = action
                  if beta <= alpha:
                      return minEval, bestAction
            return minEval, bestAction

    def make_move(self, board: Board):
        self.minimax(self.nextColor, board, 0)

    def getAllLegalMoves(self, color: str, board: Board):
        movableP = super().getMovablePieces(board, color)
        allMoves = []
        allCaptures = []
        for tup in movableP:
          space, file, rank = tup
          piece = board.getPiece(space)
          moves, captures = self.getLegalMoves(board, piece, file, rank)
          moves = list(map(lambda x: (file, rank, *x), moves))
          captures = list(map(lambda x: (file, rank, *x), captures))
          allMoves.append(moves)
          allCaptures.append(captures)
        return allMoves, allCaptures
