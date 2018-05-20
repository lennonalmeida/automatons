alfabeto = ['if','import','input']
while True:
    word = input("Palavra:  ")
    if word == alfabeto[0] or word == alfabeto[1] or word == alfabeto[2]:
        print("Accept")
    else:
        print("Reject")
