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

class ScrabbleScreen:
    def __init__(self, intLetterArray):
        self.intLetterArray = intLetterArray
        
    def updateLetterArray(self, newIntLetterArray):
        self.intLetterArray = newIntLetterArray
        
    def printScreen(self):
        cmdLinePrintScreen(self.intLetterArray)


if __name__ == "__main__":
    intLetterArray = np.ones((10, 10), int) * ord(symbolDict["hiddenChar"])
    SScreen = ScrabbleScreen(intLetterArray)
    SScreen.printScreen()


