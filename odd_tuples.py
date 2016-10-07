def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    new_tuple = ()
    for x in range(0,len(aTup)): 
        if x % 2 == 0:
            (new_tuple) += (aTup[x],)
        x+=2
    print(new_tuple)

oddTuples(("Hello", "world", "how", "are"," you!"))