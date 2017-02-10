##date: 05/21/2016
##programmer: Carswell
##submission: May COhPy
##program: counts the frequency of words in web text content from files

import requests as req

def prePare(ptr):
    """
    takes a gutenberg project text file and clips the head licensing
    information and the tail licensing information 
    """
    frankieStr = ""   
    
    rline = ptr.readline()
    while "*** START OF THIS" not in rline:
        rline = ptr.readline()

    while "*** END OF THIS" not in rline:
        frankieStr += rline
        rline = ptr.readline()

    return frankieStr

def wordFreq(parseThis):
    """
    wordFreq() will delete punctuation, convert all words to lower case, and
    keep the count of each word in a dictionary.
    """
    
    freq = {}
    nono = ('"', "'", '%', '$', '!', '.', '?', '-', ','
            , '\n', '\t', '\r', ':', ';')

    for c in nono:
        parseThis = parseThis.replace(c, " ")
        
    words = parseThis.split()
    
    for word in words:
        temp = word.lower()
        freq[temp] = freq.get(temp, 0) + 1

    return freq

def printWds(webDict):
    """
    printWds() takes the dictionary of frequency counts and sorts and
    prints the results. A lambda is used to create a list of the top
    10 word frequencies then print the frequency from the dictionary.
    """
    topEntries = sorted(webDict, key=lambda k: (-webDict[k], k))
    byFreq = sorted(webDict.values(), reverse=True)

##    print(topEntries[:10])

    print(byFreq[:10])

    for wd in topEntries[:10]:
        print("\t", wd, " <=> ", webDict[wd])

def main():
    chExit = 'n'
    fPtr = None
    processStr = None

    while chExit != 'y':

        openFile = input("What text file do you want to process? ")

        try:
            fPtr = open(openFile, "r")
                          
            processStr = prePare(fPtr)

            wordCnt = wordFreq(processStr)

            printWds(wordCnt)
        
        except IOError as err:
            print(err)
  

        chExit = input("Do you want to exit the program? (y|n) ")

if __name__ == "__main__":
    main()


