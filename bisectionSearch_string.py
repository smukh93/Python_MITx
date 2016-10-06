def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == "":
        return False
    if len(aStr)==1:
        return aStr == char
    mid = int((len(aStr))/2)
    if char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return isIn(char,aStr[:mid])
    else:
        return isIn(char, aStr[mid+1:])
    
    
def binarySearch(char, aStr, low, high):
    
    mid = int((low+high)/2)
    if char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return binarySearch(char, aStr, low, mid-1)
    elif char > aStr[mid]:
        return binarySearch(char, aStr, mid+1, high)
    else:
        return False
        

    
if binarySearch("o", "Hello", 0, len("Hello"))==1:
    print ("FOund")