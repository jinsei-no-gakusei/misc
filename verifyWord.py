def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    a = ''
    if userWord in listOfAdjs:
        a = '[ADJ]'
        
    elif userWord in listofNouns:
        a = '[NOUN]'
        
    elif userWord in listOfVerbs:
        a = '[VERB]'
        
    if madTemplate == a:
        return True
    else:
        return False