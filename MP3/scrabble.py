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




