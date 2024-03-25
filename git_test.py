arv = int(input("Sisestage arv: "))
sõne = input('Sisestage sõne: ')

for i in range(arv):
    try:
        print(sõne[i], end=' - ')
        print("Javier on äge!!!")
    except IndexError:
        break