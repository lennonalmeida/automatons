n = 0

while n == 0:
    entrada = input('Entre com palavra for or range: ')

    if entrada[0:1] == 'f':
        estado = 1
        # print('q0 > q1')
        if entrada [1:2] == "o":
            estado = 7
            # print ('q1 > q7')
            if entrada [2:3] == "r":
                estado = 6
                if len(entrada) < 4:
                    print ('q0 > q1 > q7 > q6 (final)')
                    print('for')
                    n = 1
                else:
                    print('erro caractere a mais, para no q7')
                    print('(q0 > q1 > q7)paramos no estado q7')
                    print("fo")
            else:
                    print('(q0 > q1 > q7)paramos no estado q7')
                    print("fo")
        else:
            print('(q0 > q1)paramos no estado q1')
            print("f")
    else:
        print("Erro paramos no estado q0(entrada incorreta)")
        
        if entrada [0:1] == 'r':
            estado = 2
            if entrada [1:2] == 'a':
                estado = 12
                if entrada [2:3] == 'n':
                    estado = 13
                    if entrada [3:4] == 'g':
                        estado = 8
                        if entrada [4:5] == 'e':
                            estado = 6
                            if len(entrada) < 6:
                                print('q0 > q2 > q12 > q13 > q8 > q6 ')
                                print('range')
                                n=1
                            else:
                                print('erro caractere ha mais ou incorreto ')
                                print('q0 > q2 > q12 > q13 > q8')
                                print('rang')
                        else:
                            print('q0 > q2 > q12 > q13 > q8')
                            print('rang')
                    else:
                        print('q0 > q2 > q12 > q13')
                        print('ran')
                else:
                    print('q0 > q2 > q12')
                    print('ra')
            else:
                print('q0 > q2')
                print('r')
        else:
            print('q0')
            print('estado intacto')
                                
            
