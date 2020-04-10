# +
import pytest
import pandas as pd
import numpy as np
import numpy.testing as nptest

from scrabble import ScrabbleLetters
# -

testLettersDataFrame = pd.DataFrame()
testLettersDataFrame["Letter"] = [" ", "I", "A"]
testLettersDataFrame["Count"] = [2, 2, 5]
testLettersDataFrame["Points"] = [0, 3, 5]


def test_initalizeIntLettersArrayFromDataFrame():
    scrbl_letters = ScrabbleLetters()
    
    intLetterArray = scrbl_letters.initalizeIntLettersArrayFromDataFrame(testLettersDataFrame)
    correctIntLetterArray = np.array([[ord(" "), ord(" "), ord("A")],
                                        [ord("A"), ord("A"), ord("A")],
                                        [ord("A"), ord("I"), ord("I")]])
                                        
    nptest.assert_array_equal(intLetterArray, correctIntLetterArray)
    
    del scrbl_letters
# -





