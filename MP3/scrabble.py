import numpy as np
from scrbl_interface import ScrabbleScreen
import pandas as pd


class ScrabbleLetters:

    def __init__(self, fileNameLetterCSV=None):
        if fileNameLetterCSV is not None:
            self.letter_df = loadLettersDataFrameFromFile(fileNameLetterCSV)
            self.intLetterArray = initalizeIntLettersArrayFromDataFrame(self.letter_df)
            self.screen = ScrabbleScreen(self.intLetterArray)
    
    def loadLettersDataFrameFromFile(self, fileNameLetterCV):
        letter_df = pd.read_csv(fileNameLetterCSV)
        return letter_df
        
    def initalizeIntLettersArrayFromDataFrame(self, letter_df):
        letter_df.sort_values("Letter", inplace=True)
        intLetterList = []
        for letter, count in zip(letter_df["Letter"], letter_df["Count"]):
            intLetterList += [ord(letter)] * count

        nRow = int(np.ceil(np.sqrt(len(intLetterList))))
        nCols = int(np.ceil(len(intLetterList)/nRow))

        intLetterArray = np.array(intLetterList)
        intLetterArray = np.reshape(intLetterArray,(nRow,nCols))
        return intLetterArray
    
    def showScreen():
        screen.printScreen()
        
    def shiftBy(self, shifts, axis=0):
        if np.size(self.letterArray, axis=axis) != len(shifts):
            raise ValueError("length of shifts does not equal length of array along axis")
            return


        transposedLetterArray = self.letterArray.transpose((int(1==axis), int(0==axis)))

        for iRow, shift in enumerate(shifts):
            transposedLetterArray[iRow, :] = np.roll(transposedLetterArray[iRow, :], shift)

        self.letterArray = transposedLetterArray.transpose((int(1==axis), int(0==axis)))
        
    def swapEveryN(self, n, axis=0):
        transposedLetterArray = self.letterArray.transpose((int(1==axis), int(0==axis)))

        nSwaps = len(transposedLetterArray)//n
        for iSwap in range(nSwaps):
            transposedLetterArray[:, [iSwap, iSwap+n]] = transposedLetterArray[:, [iSwap+n, iSwap]]


        self.letterArray = transposedLetterArray.transpose((int(1==axis), int(0==axis)))
