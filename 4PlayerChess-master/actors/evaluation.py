import sys
sys.path.append('./4PlayerChess-master/')
from gui.board import Board
from gui.boardStruct import BoardStruct

RED, BLUE, YELLOW, GREEN, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING = range(10)

class Evaluation():

    def evaluateBoard(self, color):
        evalValue = 0
        if color in (RED, YELLOW):
            evalValue = evalValue + (self.pieceValues(RED) + self.pieceValues(YELLOW)) - (
                    self.pieceValues(BLUE) + self.pieceValues(GREEN))
            evalValue = evalValue + (self.kingSafteyVal(BLUE) + self.kingSafteyVal(GREEN)) - (
                    self.kingSafteyVal(RED) + self.kingSafteyVal(YELLOW))
        else:
            evalValue = evalValue + (self.pieceValues(BLUE) + self.pieceValues(GREEN)) - (
                        self.pieceValues(RED) + self.pieceValues(YELLOW))
            evalValue = evalValue + (self.kingSafteyVal(RED) + self.kingSafteyVal(YELLOW)) - (
                        self.kingSafteyVal(BLUE) + self.kingSafteyVal(GREEN))

        return evalValue


    def pieceValues(self, color):
        totPVal = 0
        totPVal = totPVal + (len(self.getSquares(self.pieceSet(color, PAWN))) * 10)
        totPVal = totPVal + (len(self.getSquares(self.pieceSet(color, KNIGHT))) * 30)
        totPVal = totPVal + (len(self.getSquares(self.pieceSet(color, BISHOP))) * 35)
        totPVal = totPVal + (len(self.getSquares(self.pieceSet(color, ROOK))) * 50)
        totPVal = totPVal + (len(self.getSquares(self.pieceSet(color, QUEEN))) * 90)
        return totPVal

    # want low king saftey val, 0 = king fully protected, no attackers
    def kingSafteyVal(self, color):
        kingSquare = self.bitScanForward(self.pieceSet(color, KING))
        kingFile, kingRank = self.fileRank(kingSquare)
        KSV = 5 * self.attackersValue(kingFile, kingRank, color)
        # get squares around the king, if protected(occupied by friendly piece) + 0, if protected but attacked + attackers value
        # if unprotected + 10 if unprotected and attacked + 2 * attackers value
        for protSquare in self.getProtectedSquaresAround(kingFile, kingRank, color):
            KSV = KSV + self.attackersValue(protSquare[0], protSquare[1], color)

        for unProtSquare in self.getUnprotectedSquaresAround(kingFile, kingRank, color):
            if self.attackersValue(unProtSquare[0], unProtSquare[1], color) == 0:
                KSV = KSV + 10
            else:
                KSV = KSV + 2 * self.attackersValue(unProtSquare[0], unProtSquare[1], color)
        return KSV

