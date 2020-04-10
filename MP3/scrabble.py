import numpy as np
from scrbl_interface import ScrabbleScreen
import pandas as pd

fileNameLetterCSV = "no_scrabble_letters.csv"
letter_df = pd.read_csv(fileNameLetterCSV)
letter_df.sort_values("Letter", inplace=True)
letter_df.head()

# +
letterList = []
for letter, count in zip(letter_df["Letter"], letter_df["Count"]):
    letterList += [ord(letter)] * count

letterArray = np.array(letterList)
letterArray = np.reshape(letterArray,(10,10))
letterArray
# -

screen = ScrabbleScreen()
screen.updateLetterArray(letterArray)
screen.printScreen()

screen.printScreen()


def shiftBy(letterArray, shifts, axis=0):
    if np.size(letterArray, axis=axis) != len(shifts):
        raise ValueError("length of shifts does not equal length of array along axis")
        return
    
    
    transposedLetterArray = letterArray.transpose((int(1==axis), int(0==axis)))
    
    for iRow, shift in enumerate(shifts):
        transposedLetterArray[iRow, :] = np.roll(transposedLetterArray[iRow, :], shift)
        
    letterArray = transposedLetterArray.transpose((int(1==axis), int(0==axis)))
    

def swap_every_n(letterArray, n, axis=0):
    transposedLetterArray = letterArray.transpose((int(1==axis), int(0==axis)))
    
    nSwaps = len(transposedLetterArray)//n
    for iSwap in range(nSwaps):
        transposedLetterArray[:, [iSwap, iSwap+n]] = transposedLetterArray[:, [iSwap+n, iSwap]]
        
    
    letterArray = transposedLetterArray.transpose((int(1==axis), int(0==axis)))
        

swap_every_n(letterArray, 2, axis=1)
screen.printScreen()

shiftBy(letterArray, [0,1,2,3,4,5,6,7,8,9], axis=1)
shiftedletterArray

screen.printScreen()

screen.updateLetterArray(shiftedletterArray)
screen.printScreen()

screen.updateLetterArray(shiftedletterArray)
screen.printScreen()

axis = 0
for letters in letterArray.transpose((int(1==axis), int(0==axis))):
    print(letters)




