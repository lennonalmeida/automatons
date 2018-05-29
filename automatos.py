
def state(word):
    #se nao formar palavra state = This word dont belong to our alphabet
    #
    first = word[0:1]
    if first == 'f':
        #or
    elif first == 'o':
        #r
    elif first == 'i':
        #s or n
    elif first == 'n':
        #ot
    elif first == 'a':
        #s or nd
    elif first == 'd':
        #ef or el
    elif first == 't':
        #ry
    else:
        state = 'This word dont belong to our alphabet'

    return state

#main code
wd = input("Word to be verfied:")
state_out = state(wd)
print(state_out)
