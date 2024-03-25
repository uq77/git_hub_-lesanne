arv = int(input("Sisestage arv: "))
sõne = input('Sisestage sõne: ')

for i in range(arv):
    try:
        print(sõne[i], end='-')
    except IndexError:
        print("\narv on sõnest suurem")
        break