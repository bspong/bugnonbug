from nltk.tokenize import word_tokenize

################################################################################
################################################################################
################################################################################
#   ######  Do!! #####
#               - Tokenization by Computer Dictionary
#
################################################################################
################################################################################
################################################################################
################################################################################


def fileRead(fileName):
    fileContents = open(fileName, 'r').read()
    return fileContents


fileName = 'text.txt'
Textcontent = fileRead(fileName)

################### Normal ToKen ###################
normalToken = Textcontent.split()
print (normalToken)

# print('\n\n')
# print (Textcontent.split(' ', 1))
print ('\n\n')
################### Dictionary ToKen with Library ###################
dicToken = word_tokenize(Textcontent)
print (dicToken)

print ('\n')
print ('nomal : '+ str(len(normalToken)))
print ('dict : '+ str(len(dicToken)))

i=0

newWord = []
roundCheck = len(dicToken)
for nToken in normalToken:
    countRoundCheck = 0
    for dToken in dicToken:
        if dToken == nToken:
            i=i+1
            break
        else:
            countRoundCheck=countRoundCheck+1
           # print (countRoundCheck)
    if countRoundCheck == roundCheck:
        newWord.append(nToken)
            
    
print('nomal==dict : ' + str(i) + '\nnomal!=dict : '  + str(len(newWord)))
print (newWord)
                





