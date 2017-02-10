##date: 05/21/2016
##programmer: Carswell
##submission: May COhPy
##program: counts the frequency of words in web text content

import requests as req

def prePare(aStr):
    """
    do two splits to get the middle
    """
    
    headTest = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    tailTest = "*** END OF THIS PROJECT GUTENBERG EBOOK"

    head = aStr.split(headTest)
    tail = head[1].split(tailTest)

    return tail[0]

    
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

    print(byFreq[:10])

    for wd in topEntries[:10]:
        print("\t", wd, " :: ", webDict[wd])

def main():
    chExit = 'n'

    while chExit != 'y':

        webAddr = input("What web text file do you want to process? ")

        reqText = req.get(webAddr)

        if reqText.status_code >= 200 and reqText.status_code < 300:
            if 'text/plain' in reqText.headers['content-type']:
                
                printWds(wordFreq(prePare(reqText.text)))

            else:
                print("Not text content")
        else:
            print("Unsuccessful!")


        chExit = input("Do you want to exit the program? (y|n) ")

if __name__ == "__main__":
    main()

