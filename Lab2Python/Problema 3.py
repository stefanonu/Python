#Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian.
#Sa se scrie o functie care primeste ca parametru o lista de puncte
#si returneaza o lista de tuple (a,b,c) unice care reprezinta
#dreptele unice determinate de acele puncte ( (a,b,c) corespunde
#dreptei ax + by + c = 0).

def puncte(tuple_list_x_y):
    for iterator in tuple_list_x_y:
        