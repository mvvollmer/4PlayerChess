import sys
import random
from collections import deque

sys.path.append('./4PlayerChess-master/')
from gui.board import Board
from actors.strategy import Strategy
from actors.moveOrdering import mvv_lva, KillerMoves, GlobalHistoryHeuristic
from actors.evaluation import EvalBase


class MinimaxStrategy(Strategy):
    # self.eval = evaluation()
    def __init__(self, player: str, maxDepth: int, eval: EvalBase, globalHistory: GlobalHistoryHeuristic):
        super().__init__(player)
        self.maxDepth = maxDepth
        self.history = globalHistory
        self.killerMoves = KillerMoves(maxDepth)
        self.evaluation = eval
        self.nextColor = deque(['r', 'b', 'y', 'g'])
        while self.nextColor[0] != self.player:
          self.nextColor.rotate(-1)

    def negamax(self, color: str, board: Board, depth: int, alpha: float = float("-inf"), beta: float = float("inf")):
        colorNum = board.colorMapping[color]
        boardCopy = self.getNewBoard(board)
        if boardCopy.checkMate(colorNum) or depth >= self.maxDepth: # since root is depth = 0
            # print('--- separator ---')
            # print(boardCopy.boardData[:14])
            # print(boardCopy.boardData[14:28])
            # print(boardCopy.boardData[28:42])
            # print(boardCopy.boardData[42:56])
            # print(boardCopy.boardData[56:70])
            # print(boardCopy.boardData[70:84])
            # print(boardCopy.boardData[84:98])
            # print(boardCopy.boardData[98:112])
            # print(boardCopy.boardData[112:126])
            # print(boardCopy.boardData[126:140])
            # print(boardCopy.boardData[140:154])
            # print(boardCopy.boardData[154:168])
            # print(boardCopy.boardData[168:182])
            # print(boardCopy.boardData[182:196])
            # print('--- end separator ---')
            return self.evaluation.evaluateBoard(colorNum, boardCopy), None
        moves, captures = self.getAllLegalMoves(color, boardCopy)
        orderedCaptures = mvv_lva(captures, boardCopy)
        orderedMoves = self.history.sortMoves(moves)
        orderedMoves = self.killerMoves.sortMoves(moves, depth)
        actions = orderedCaptures + orderedMoves
        maxEval = float("-inf")
        bestAction = None
        for action in actions:
            # print('---BEFORE---')
            # print(boardCopy.boardData[:14])
            # print(boardCopy.boardData[14:28])
            # print(boardCopy.boardData[28:42])
            # print(boardCopy.boardData[42:56])
            # print(boardCopy.boardData[56:70])
            # print(boardCopy.boardData[70:84])
            # print(boardCopy.boardData[84:98])
            # print(boardCopy.boardData[98:112])
            # print(boardCopy.boardData[112:126])
            # print(boardCopy.boardData[126:140])
            # print(boardCopy.boardData[140:154])
            # print(boardCopy.boardData[154:168])
            # print(boardCopy.boardData[168:182])
            # print(boardCopy.boardData[182:196])
            # print('--- Action ---')
            # print(action)
            nextBoardState = self.getNewBoard(boardCopy)
            nextBoardState.makeMove(*action)
            self.nextColor.rotate(-1) # this code might not work
            eval, _ = self.negamax(self.nextColor[0], nextBoardState, depth + 1, -beta, -alpha)
            eval = -eval
            self.nextColor.rotate(1)
            if eval > maxEval:
              maxEval = eval
              bestAction = action
              alpha = max(alpha, eval)
            if maxEval >= beta:
                self.killerMoves.store_move(bestAction, depth)
                self.history.store_move(bestAction, depth)
                return maxEval, bestAction
        return maxEval, bestAction

    def make_move(self, board: Board):
        _, action = self.negamax(self.nextColor[0], board, 0)
        # update global history depth
        self.history.incrementGlobalDepth()
        # print('minimax mover')
        # print('official move:', *action)
        return action

