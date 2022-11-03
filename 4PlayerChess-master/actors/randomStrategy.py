import sys
import random

sys.path.append('./4PlayerChess-master/')
from actors.strategy import Strategy
from gui.board import Board


class RandomStrategy(Strategy):
  def __init__(self, player):
    super().__init__(player)
  def make_move(self, board: Board):
    movableP = super().getMovablePieces(board)
    space, file, rank = random.choice(movableP)
    piece = board.getPiece(space)
    moves, captures = self.getLegalMoves(board, piece, file, rank)
    poss_moves = moves + captures
    toFile, toRank = random.choice(poss_moves)
    return file, rank, toFile, toRank




# Notes:
# Board is a bunch of strings, pieces written as 2 parts _ _, first blank is color
# [r, g, b, y] and second blank is piece [R, N, B, Q, K, P]
# board is built as expected, only note is that first few rows are red pieces, meaning
# array is down to up (if that makes any sense, see printouts below)
# file: x-coord, rank: y-coord
# print(board.boardData[:14])
# print(board.boardData[14:28])
# print(board.boardData[28:42])
# print(board.boardData[42:56])
# print(board.boardData[56:70])
# print(board.boardData[70:84])
# print(board.boardData[84:98])
# print(board.boardData[98:112])
# print(board.boardData[112:126])
# print(board.boardData[126:140])
# print(board.boardData[140:154])
# print(board.boardData[154:168])
# print(board.boardData[168:182])
# print(board.boardData[182:196])