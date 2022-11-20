from numpy import deprecate_with_doc
from gui.board import Board
from actors.strategy import Strategy
import actor
import sys
import random

sys.path.append('./4PlayerChess-master/')


class Minimax(Strategy):
    # self.eval = evaluation()
    def __init__(self, actor, depth):
        super().__init__(actor, "minimax")
        self.depth = depth

    def minimax(self, color: actor, board: Board, depth: int, alpha: float = "-inf", beta: float = "-inf"):
        if board.checkMate(color):
            return evaluation(board)

        if maximizing_player:
            maxEval = "-inf"
            for square in board.getSquares:
                eval = minimax(square, depth - 1, alpha, beta)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = "inf"
            for square in board.getSquares:
                eval = minimax(square, depth - 1, alpha, beta)
                minEval = min(minEval, eval)
                if beta <= alpha:
                    break
            return minEval

    def make_move(self, board: Board):
        moveableP = super().getMovablePieces(board)
