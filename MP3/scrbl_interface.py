import numpy as np

# +
symbolDict = {"hLine": "----", "vLine": "|", "spacing": " ", "hiddenChar": "*"}


def cmdLinePrintScreen(charArray):
    nX, nY = charArray.shape
    vSepString = symbolDict["spacing"] + symbolDict["vLine"] + symbolDict["spacing"]
    hSepString = symbolDict["vLine"]+symbolDict["hLine"]*(nY-1)+symbolDict["hLine"][:-1]+symbolDict["vLine"]
    for iX in range(nX):
        print(hSepString)
        print(vSepString[1:], end="")
        stringRow = vSepString.join(chr(x) for x in charArray[iX, :])
        print(stringRow, end="")
        print(vSepString[:2])
    print(hSepString)
    return


# -

thing = np.ones((5,3), int) * 100;
print(thing)
cmdLinePrintScreen(thing)


class ScrabbleScreen:
    def __init__(self, nTiles=100):
        nRows = int(np.ceil(np.sqrt(nTiles)))
        nCols = int(np.ceil(nTiles/nRows))
        self.intLetterArray = np.ones((nRows, nCols), int) * ord(symbolDict["hiddenChar"])
        
    def updateLetterArray(newIntLetterArray):
        self.intLetterArray = newIntLetterArray
        
    def printScreen(self):
        cmdLinePrintScreen(self.intLetterArray)
        


SScreen = ScrabbleScreen()
SScreen.printScreen()


