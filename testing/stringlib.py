def letterCount(myStr, letter):
    if len(myStr) <= 0 or len(letter) <= 0:
        return 0
    return myStr.count(letter)

def removeSpace(myStr):
    return myStr.replace(" ", "")
