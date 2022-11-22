import sys
sys.path.append('./4PlayerChess-master/')
from gui.board import Board
from gui.boardStruct import BoardStruct

RED, BLUE, YELLOW, GREEN, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING = range(10)

class Evaluation():

    def evaluateBoard(self, color: int, board: Board):
        evalValue = 0
        if color in (RED, YELLOW):
            evalValue = evalValue + (self.pieceValues(RED, board) + self.pieceValues(YELLOW, board)) - (
                    self.pieceValues(BLUE, board) + self.pieceValues(GREEN, board))
            evalValue = evalValue + (self.kingSafetyVal(BLUE, board) + self.kingSafetyVal(GREEN, board)) - (
                    self.kingSafetyVal(RED, board) + self.kingSafetyVal(YELLOW, board))
        else:
            evalValue = evalValue + (self.pieceValues(BLUE, board) + self.pieceValues(GREEN, board)) - (
                        self.pieceValues(RED, board) + self.pieceValues(YELLOW, board))
            evalValue = evalValue + (self.kingSafetyVal(RED, board) + self.kingSafetyVal(YELLOW, board)) - (
                        self.kingSafetyVal(BLUE, board) + self.kingSafetyVal(GREEN, board))

        return evalValue


    def pieceValues(self, color: int, board: Board):
        totPVal = 0
        totPVal = totPVal + (len(board.getSquares(board.pieceSet(color, PAWN))) * 10)
        totPVal = totPVal + (len(board.getSquares(board.pieceSet(color, KNIGHT))) * 30)
        totPVal = totPVal + (len(board.getSquares(board.pieceSet(color, BISHOP))) * 35)
        totPVal = totPVal + (len(board.getSquares(board.pieceSet(color, ROOK))) * 50)
        totPVal = totPVal + (len(board.getSquares(board.pieceSet(color, QUEEN))) * 90)
        return totPVal

    # want low king saftey val, 0 = king fully protected, no attackers
    def kingSafetyVal(self, color: int, board: Board):
        # print(color)
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
        # board.printBB(board.pieceSet(color, KING))
        # print('in between')
        # print(board.bitScanForward(board.pieceSet(color, KING)))
        kingSquare = board.bitScanForward(board.pieceSet(color, KING))
        kingFile, kingRank = board.fileRank(kingSquare)
        KSV = 5 * board.attackersValue(kingFile, kingRank, color)
        # get squares around the king, if protected(occupied by friendly piece) + 0, if protected but attacked + attackers value
        # if unprotected + 10 if unprotected and attacked + 2 * attackers value
        for protSquare in board.getProtectedSquaresAround(kingFile, kingRank, color):
            KSV = KSV + board.attackersValue(protSquare[0], protSquare[1], color)

        for unProtSquare in board.getUnprotectedSquaresAround(kingFile, kingRank, color):
            if board.attackersValue(unProtSquare[0], unProtSquare[1], color) == 0:
                KSV = KSV + 10
            else:
                KSV = KSV + 2 * board.attackersValue(unProtSquare[0], unProtSquare[1], color)
        return KSV

