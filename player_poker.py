import random


class Player:
    lista_culori = ['Treflaa', 'Rombb', 'Inima Neagraa', 'Inima Rosiee']
    lista_numere = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    lista_carti = []
    for i in range(0, 13):
        for j in range(0, 4):
            lista_carti.append((lista_numere[i], lista_culori[j]))
    mana_carti = {}

    def __init__(self, nume_jucator, suma_bani):
        self.nume_jucator = nume_jucator
        self.suma_bani = suma_bani
        self.mana_carti = {}

    def __repr__(self):
        return f'{self.nume_jucator}-{self.suma_bani}|'

    def bet(self, suma_bet, suma_actuala, last_bet, runda):
        if runda == 0:
            print(f'{self.nume_jucator} a pariat {suma_bet}.\n')
            self.suma_bani -= suma_bet
        elif suma_bet > last_bet:
            print(f'{self.nume_jucator} a dat Raise cu {suma_bet - last_bet}. A pariat {suma_bet}.\n')
            self.suma_bani -= suma_bet
            return [suma_bet + suma_actuala, suma_bet]
        elif suma_bet == last_bet:
            print(f'{self.nume_jucator} a dat Call.\n')
            self.suma_bani -= suma_bet
        elif suma_bet == 0:
            print(f'{self.nume_jucator} a dat Check.\n')
        #print(self.suma_bani)
        return [suma_bet + suma_actuala, suma_bet]

    def all_in(self):
        print(f'{self.nume_jucator} a dat All In!\n')
        suma_bet = self.suma_bani
        self.suma_bani = 0
        return suma_bet

    def alegere_carti(self, val, lista_carti=None):
        '''carte = list(Player.lista_carti.keys())
        culoare = list(Player.lista_carti.values())
        if x == 0:
            self.mana_carti = [{random.choice(carte): random.choice(culoare[random.randint(0, 12)])},
                               {random.choice(carte): random.choice(culoare[random.randint(0, 12)])},
                               {random.choice(carte): random.choice(culoare[random.randint(0, 12)])}]
        elif x == 1:
            self.mana_carti = [{random.choice(carte): random.choice(culoare[random.randint(0, 12)])},
                               {random.choice(carte): random.choice(culoare[random.randint(0, 12)])}]
        else:
            self.mana_carti = [{random.choice(carte): random.choice(culoare[random.randint(0, 12)])}]
        return self.mana_carti'''
        if val == 0:
            x = 3
            while x > 0:
                alegere = random.choice(lista_carti)
                Player.lista_carti.remove(alegere)
                carte = alegere[0]
                culoare = alegere[1]
                if carte in Player.mana_carti.keys():
                    nr = random.choice(['1', '2', '3', '4', '5'])
                    carte += nr
                Player.mana_carti.update({carte: culoare})
                x -= 1
            return (Player.mana_carti, Player.lista_carti)

        elif val == 1:
            x = 2
            while x > 0:
                alegere = random.choice(Player.lista_carti)
                Player.lista_carti.remove(alegere)
                carte = alegere[0]
                culoare = alegere[1]
                if carte in self.mana_carti.keys():
                    nr = random.choice(['1', '2', '3', '4', '5'])
                    carte += nr
                self.mana_carti.update({carte: culoare})
                x -= 1
            return (self.mana_carti, Player.lista_carti)
        else:
            alegere = random.choice(lista_carti)
            Player.lista_carti.remove(alegere)
            carte = alegere[0]
            culoare = alegere[1]
            if carte in Player.mana_carti.keys():
                nr = random.choice(['1', '2', '3', '4', '5'])
                carte += nr
            Player.mana_carti.update({carte: culoare})
            return (Player.mana_carti, Player.lista_carti)


    def fold(self):
        print(f'{self.nume_jucator} a dat fold.')
        self.mana_carti = []
        return self.mana_carti

'''def choose():
    nume_jucator = input('Introduceti numele pentru a participa in joc:\n').title()
    suma_bani = int(input('Cu ce suma intrati in concurs?\n'))
    jucator = Player(nume_jucator, suma_bani)
    var1 = Player('Dragos', suma_bani)
    var2 = Player('Razvan', suma_bani)
    var3 = Player('Robert', suma_bani)
    lista_jucatori = [var1, var2, var3, jucator]
    return lista_jucatori

a = choose()
x = a[0].alegere_carti(1)
y = a[0].alegere_carti(0)
z = a[1].alegere_carti(0)
print(x, z, len(Player.lista_carti))'''