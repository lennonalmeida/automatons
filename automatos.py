
def state(word):
    #se nao formar palavra state = This word dont belong to our alphabet
    reject = 'This word dont belong to our alphabet'
    accepted = ' | Accepted'
    first = word[0:1]
    if first == 'f':
        state = 'hell'
    #     #or
    # elif first == 'o':
    #     #r
    # elif first == 'i':
    #     #s or n
    # elif first == 'n':
    #     #ot
    elif first == 'a':
        #s or nd
        state = 'q0->q1'
        if word[1:2] == 's':
            state += '->q13'
            if len(word)>2:
                state = reject
            else:
                state+=accepted
        elif word[1:2] == 'n':
            state +=  '->q2'
            if word[2:3] == 'd':
                state += '->q3'
                if len(word) > 3:
                    state = reject
                else:
                    state+=accepted
            else:
                state+=' | '+reject
        else:
            state += ' | '+reject

    elif first == 'd':
        #ef or el
        state = 'q0->q6'
        if word[1:2] == 'e':
            state+='->q4'
            if word[2:3] == 'f':
                if len(word) > 3:
                    state = reject
                else:
                    state += '->q7' + accepted
            elif word[2:3] == 'l':
                if len(word) > 3:
                    state = reject
                else:
                    state += '->q3' + accepted
            else:
                state +=' | ' + reject
        else:
            state +=' | '+ reject
    elif first == 't':
         #ry
         state = 'q0->q10'
         if word[1:2] == 'r':
             state += '->q11'
             if word[2:3] == 'y':
                 state += '->q3'
                 if len(word)>3:
                     state = reject
                 else:
                    state+=accepted
             else:
                 state += ' | '+reject
         else:
             state +=' | '+ reject
    else:
        state = reject

    return state

#main code
print("Press CTRL+C to interrupt the program")
print("Initial state: q0\nFinal states: q3, q14, q13, q7\n")
while True:
    try:
        wd = input("Word to be verfied:")
        state_out = state(wd)
        print(state_out)
        print("-------------------------")
    except KeyboardInterrupt:
        print("CTRL-C pressed")
        break
