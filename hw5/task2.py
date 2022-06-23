# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? 
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 

print("Let's get the game started!\n")

table = list(range(1, 10))

def show_table(tab):
    print("-"*13)
    for i in range(3):
        print("|", tab[0+i*3], "|", tab[1+i*3], "|", tab[2+i*3])
        print("-"*13)

show_table(table)