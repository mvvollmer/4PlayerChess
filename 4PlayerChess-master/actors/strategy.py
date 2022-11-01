import sys
sys.path.append('./4PlayerChess-master/')
from gui.board import Board

class Strategy():
  def __init__(self, player):
    self.player = player
  def make_move(self, board: Board):
    # Make a move given the board state. Note, not handled in our implementation is the duplication
    # of gameboard and validation of moves from an AI actor. We just assume that these are valid and
    # pass the actual gameboard to the actor to allow them to move. 
    pass

  def getLegalMoves(self, board: Board, piece: int, fromFile: int, fromRank: int):
    # get legal moves for a piece given the board state. Taken from view function.
    # TODO: check that when en-passant and checks/checkmates are working that the board functions used here
    #       still work
    origin = board.square(fromFile, fromRank)
    moves = board.getSquares(board.legalMoves(piece, origin, board.colorMapping[self.player]) & board.emptyBB)
    captures = board.getSquares(board.legalMoves(piece, origin, board.colorMapping[self.player]) &
                                      board.occupiedBB)
    return moves, captures

  def getMovablePieces(self, board: Board):
    # get the pieces which can move for this player
    moveable_pieces = []
    for i, space in enumerate(board.boardData):
      if space[0] == self.player:
        file, rank = board.indexToFileRank(i)
        piece = board.getPiece(space)
        moves, captures = self.getLegalMoves(board, piece, file, rank)
        if len(moves) != 0 or len(captures) != 0:
          moveable_pieces.append((space, file, rank))
    return moveable_pieces

  # TODO: potentially add function for promote requests