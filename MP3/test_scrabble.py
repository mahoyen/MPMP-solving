# +
import pytest
import pandas as pd
import numpy as np
import numpy.testing as nptest

from scrabble import ScrabbleLetters
# -
# +
testLettersDataFrame = pd.DataFrame()
testLettersDataFrame["Letter"] = [" ", "I", "A"]
testLettersDataFrame["Count"] = [2, 2, 5]
testLettersDataFrame["Points"] = [0, 3, 5]

correctIntLetterArray = np.array([[ord(" "), ord(" "), ord("A")],
                                        [ord("A"), ord("A"), ord("A")],
                                        [ord("A"), ord("I"), ord("I")]])

        

# -
# +

def test_initalizeIntLettersArrayFromDataFrame():
    # Setup
    scrbl_letters = ScrabbleLetters()
    
    # Test
    intLetterArray = scrbl_letters.initalizeIntLettersArrayFromDataFrame(testLettersDataFrame)

    # Compare                                 
    nptest.assert_array_equal(intLetterArray, correctIntLetterArray)
    
# -
# +
axis0shift000 =   np.array([[ord(" "), ord(" "), ord("A")],
                            [ord("A"), ord("A"), ord("A")],
                            [ord("A"), ord("I"), ord("I")]])
                            
axis0shift123 =   np.array([[ord("A"), ord(" "), ord(" ")],
                            [ord("A"), ord("A"), ord("A")],
                            [ord("A"), ord("I"), ord("I")]])

axis1shift123 =   np.array([[ord("A"), ord("A"), ord("A")],
                            [ord(" "), ord("I"), ord("A")],
                            [ord("A"), ord(" "), ord("I")]])

axis1shift222 =   np.array([[ord("A"), ord("A"), ord("A")],
                            [ord("A"), ord("I"), ord("I")],
                            [ord(" "), ord(" "), ord("A")]])

axis0shift222 =   np.array([[ord(" "), ord("A"), ord(" ")],
                            [ord("A"), ord("A"), ord("A")],
                            [ord("I"), ord("I"), ord("A")]])
# -
# +
@pytest.mark.parametrize("shifts,axis,expected", [([0,0,0], 0, axis0shift000),
                                                  ([1,2,3], 0, axis0shift123),
                                                  ([1,2,3], 1, axis1shift123),
                                                  ([2,2,2], 1, axis1shift222),
                                                  ([2,2,2], 0, axis0shift222),
                                                  ])
def test_shiftBy(shifts,axis,expected):
    # Setup
    scrbl_letters = ScrabbleLetters()
    scrbl_letters.intLetterArray = correctIntLetterArray.copy()

    # Test
    scrbl_letters.shiftBy(shifts, axis=axis)

    # Compare
    nptest.assert_array_equal(scrbl_letters.intLetterArray, expected)
# -
# +
axis0n0 = np.array([[ord(" "), ord(" "), ord("A")],
                    [ord("A"), ord("A"), ord("A")],
                    [ord("A"), ord("I"), ord("I")],
                    ])

axis0n1 = np.array([[ord("A"), ord("I"), ord("I")],
                    [ord("A"), ord("A"), ord("A")],
                    [ord(" "), ord(" "), ord("A")],
                    ])
                    
axis0n2 = np.array([[ord("A"), ord("A"), ord("A")],
                    [ord(" "), ord(" "), ord("A")],
                    [ord("A"), ord("I"), ord("I")]])
                    
axis1n0 = np.array([[ord(" "), ord(" "), ord("A")],
                    [ord("A"), ord("A"), ord("A")],
                    [ord("A"), ord("I"), ord("I")]])

axis1n1 = np.array([[ord("A"), ord(" "), ord(" ")],
                    [ord("A"), ord("A"), ord("A")],
                    [ord("I"), ord("I"), ord("A")]])
                    
axis1n2 = np.array([[ord(" "), ord(" "), ord("A")],
                    [ord("A"), ord("A"), ord("A")],
                    [ord("I"), ord("A"), ord("I")]])

# -
# +
@pytest.mark.parametrize("n,axis,expected",      [(0, 0, axis0n0),
                                                  (1, 0, axis0n1),
                                                  (2, 0, axis0n2),
                                                  (0, 1, axis1n0),
                                                  (1, 1, axis1n1),
                                                  (2, 1, axis1n2),
                                                  ])
def test_swapEveryN(n, axis, expected):
    # Setup
    scrbl_letters = ScrabbleLetters()
    scrbl_letters.intLetterArray = correctIntLetterArray.copy()

    # Test
    scrbl_letters.swapEveryN(n, axis=axis)

    # Compare
    nptest.assert_array_equal(scrbl_letters.intLetterArray, expected)

