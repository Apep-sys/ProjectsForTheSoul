import random
import time

class Player:
    mana_carti = []
    lista_carti = {'2': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   '3': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   '4': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   '5': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   '6': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   '7': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   '8': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   '9': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   '10': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   'A': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   'J': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   'Q': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla'],
                   'K': ['Romb', 'Inima Rosie', 'Inima Neagra', 'Trefla']}

    def __init__(self, nume_jucator, suma_bani):
        self.nume_jucator = nume_jucator
        self.suma_bani = suma_bani

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

    def alegere_carti(self, x):
        carte = list(Player.lista_carti.keys())
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
        return self.mana_carti

    def fold(self):
        print(f'{self.nume_jucator} a dat fold.')
        self.mana_carti = []
        return self.mana_carti


class Game(Player):
    """var1 = Player('Dragos', 500)
    var2 = Player('Razvan', 500)
    var3 = Player('Robert', 500)
    lista_jucatori = [var1, var2, var3"""
    jucator_principal = None
    lista_jucatori = None
    lista_pariu = [0, 2, 5, 10, 50, 100]
    table_cards = []


    def __init__(self, nume_jucator, suma_bani, lista_jucatori):
        super().__init__(nume_jucator, suma_bani)
        Game.lista_jucatori = lista_jucatori
        Game.jucator_principal = lista_jucatori[3]

    def dealing(self, x):
        global y
        if x == 0:
            print('Cartile vor fi acum impartite!\n... ... ...')
            for x in Game.lista_jucatori:
                y = x.alegere_carti(1)
                x.mana_carti.append(y)
                x.mana_carti.pop()[1]
            print('Mana dvs. este:', Game.lista_jucatori[3].mana_carti)
        '''print('Acum pariati!')
        for x in self.lista_jucatori:
            x.bet'''
        if x == 1:
            print('\nDealerul va da acum prima serie- Flop!')
            print('Cartile sunt:')
            y = Game.alegere_carti(self, 0)
            Game.table_cards.append(y)
            print(list(Game.table_cards[0]))
            print(list(Game.table_cards[0][0].values())[0])
        if x == 2:
            print('\nDealerul va da acum a doua serie- Turn!')
            y = Game.alegere_carti(self, 2)
            '''while True:
                try:
                    if y in temporary_cards:
                        continue
                except:
                    pass'''
            Game.table_cards.append(y)
            print(Game.table_cards)
        if x == 3:
            print('\nDealerul va da acum ultima serie- River!')
            y = Game.alegere_carti(self, 2)
            Game.table_cards.append(y)
            print(Game.table_cards)
        temporary_cards = Game.table_cards
        return Game.table_cards

    def runda0(self, suma_actuala):
        global pariu_introdus
        big_blind = 2
        small_blind = 1
        pariu_mare = big_blind  # Cazul in care abia a inceput runda si s-au dat cartile!
        big_b = Game.lista_jucatori[0].bet(big_blind, suma_actuala, big_blind, 0)
        small_b = Game.lista_jucatori[1].bet(small_blind, big_b[0], pariu_mare, 0)
        suma_actuala = small_b[0]
        #bb[0] e noua suma si bb[1] ultimul bet
        lista_temporara = Game.lista_jucatori[2:4]
        for turn in lista_temporara:
            pariu_runda_0 = pariu_mare
            if turn.nume_jucator == Game.jucator_principal.nume_jucator:
                print(f'Pariati {pariu_mare} sau mai mult pentru a intra in joc.\nBani ramasi: {self.suma_bani}')
                while True:
                    pariu_introdus = int(input())
                    if pariu_introdus < pariu_mare:
                        while True:
                            raspuns = input('Doriti sa dati fold? Y/N: ')
                            if raspuns.title() == 'Y':
                                self.fold()
                                break
                            elif raspuns.title() == 'N':
                                break
                            else:
                                print('Raspuns invalid. Introduceti un raspuns valid.')
                                continue
                        print(f'Trebuie sa pariati o suma egala cu {pariu_mare} sau mai mare pentru a continua.')
                        continue
                    elif pariu_introdus == pariu_mare:
                        suma_calculata = turn.bet(pariu_introdus, suma_actuala, pariu_mare, 0)
                        suma_actuala = suma_calculata[0]
                    elif pariu_introdus > pariu_mare:
                        for jucator in Game.lista_jucatori[:]:
                            if jucator.nume_jucator == Game.jucator_principal:
                                suma_calculata = jucator.bet(pariu_introdus, suma_actuala, pariu_introdus, 0)
                                suma_actuala = suma_calculata[0]
                            else:
                                suma_calculata = jucator.bet(jucator.suma_bani - (Game.jucator_principal.suma_bani - pariu_introdus), suma_actuala, pariu_introdus, 0)
                                suma_actuala = suma_calculata[0]
                    break
            else:
                suma_calculata = turn.bet(Game.lista_pariu[0], suma_actuala, pariu_mare, 0)
                suma_actuala = suma_calculata[0]
        #suma_calculata = Game.lista_jucatori[1].bet(1, suma_actuala, pariu_mare, 0)
        #suma_actuala = suma_calculata[0]
        for x in Game.lista_jucatori:
            print(x.nume_jucator)
            print('NEXT', suma_actuala, x.suma_bani)
        return suma_actuala

    def runde_shuffle(self, suma_actuala):
        pariu_mare = 0
        for turn in Game.lista_jucatori:
            if turn == Game.jucator_principal and pariu_mare == 0:
                print('Alegeti suma pe care o pariati:', Game.lista_pariu, f'\nBani ramasi:{self.suma_bani}')
                pariu = int(input())
                suma_calculata = turn.bet(pariu, suma_actuala, pariu_mare, 0)
                suma_actuala = suma_calculata[0]
                pariu_mare = pariu
            elif turn != Game.jucator_principal and pariu_mare == 0:
                suma_calculata = turn.bet(random.choice(Game.lista_pariu), suma_actuala, pariu_mare, 0)
                suma_actuala = suma_calculata[0]
                pariu_mare = suma_calculata[1]
            elif turn != Game.jucator_principal and pariu_mare != 0:
                try:
                    suma_calculata = turn.bet(random.choice(Game.lista_pariu[pariu_mare:]), suma_actuala, pariu_mare, 1)
                except IndexError:
                    suma_calculata = turn.bet(pariu_mare, suma_actuala, pariu_mare, 1)
                suma_actuala = suma_calculata[0]
                pariu_mare = suma_calculata[1]
            elif turn == Game.jucator_principal and pariu_mare != 0:
                while True:
                    print(f'Bet actual: {suma_actuala}')
                    print(f'Trebuie sa pariati o suma egala cu {pariu_mare} sau mai mare pentru a continua.')
                    pariu = int(input())
                    if pariu < pariu_mare:
                        raspuns = input('Doriti sa dati fold? Y/N\n').title()
                        if raspuns == 'Y':
                            self.fold()
                            break
                        elif raspuns == 'N':
                            continue
                    else:
                        break
                suma_calculata = turn.bet(pariu, suma_actuala, pariu_mare, 1)
                suma_actuala = suma_calculata[0]
            #y = self.bet(pariu, small_b[0], small_b[1], runda)[0]
            ### DE CONTINUAT! Grija daca exista un pariu inainte sau nu.
        '''print(turn)
        x = self.lista_jucatori[turn]
        self.lista_jucatori[turn] = self.lista_jucatori[turn + 1]
        self.lista_jucatori[3] = x'''
        return suma_actuala

    def hand_ranking(self, mana_carti, table_cards):
        print(list(Game.jucator_principal.mana_carti))
        lista_valori_p, lista_culori_p = [], []
        lista_valori_n, lista_culori_n = [], []
        #royal_Flush, straight_Flush, four_Kind, full_House, flush, straight, three_kind, two_pair, pair, high_Card = 0
        for i in range(0, 2):
            lista_valori_p.append(list(mana_carti[i].keys())[0])
            print(lista_valori_p)
            lista_culori_p.append(list(mana_carti[i].values())[0])
            print(lista_culori_p)
        for i in range(0, 6):
            lista_valori_n.append(list(table_cards[0][i].keys())[0])
            lista_culori_n.append(list(table_cards[0][i].values())[0])
        for i in range(0, 2):
            for j in range(0, 6):
                if lista_valori_p[i] in lista_valori_n[j]:
                    lista_valori_n.count(j)


    def joc_poker(self):
        suma_actuala = 0
        print('Bine ati venit la Campionatul Saptamanal de Poker!')
        print(f'Jucatorii din aceasta seara sunt {self.lista_jucatori[0].nume_jucator}, '
              f'{self.lista_jucatori[1].nume_jucator}, '
              f'{self.lista_jucatori[2].nume_jucator}, {self.lista_jucatori[3].nume_jucator}')
        print(self.lista_jucatori)
        for i in range(0, 6):
            if i == 0:
                suma_actuala = self.runda0(suma_actuala)
                game_start = self.dealing(0)
                print('\nAcum pariati!')
            else:
                print('Suma actuala: ', suma_actuala)
                suma_actuala = self.runde_shuffle(suma_actuala)
                game_continue = self.dealing(i)
        for i in Game.lista_jucatori:
            Game.hand_ranking(self, i.mana_carti, Game.table_cards)
        #suma_actuala = self.turn_shuffle(suma_actuala)
        #y = self.dealing(0)
        #y = self.dealing(1)
        #suma_actuala = self.turn_shuffle(suma_actuala)
        print('\nAcum pariati!')
        '''print('Alegeti suma pe care o pariati:', Game.lista_pariu, f'\nBani ramasi:{self.suma_bani}')
        pariu = int(input())
        suma_actuala += self.bet(pariu, suma_actuala)
        print(f'Jucatorul {self.nume_jucator} a pariat {pariu}.\n')
        for x in range(0, 3):
            y = self.lista_jucatori[x].bet(random.choice(Game.lista_pariu), suma_actuala)
            suma_actuala = y
            print(f'Jucatorul {self.lista_jucatori[x]} a pariat {y}.', suma_actuala)'''



#print('********\n*  ', '10♣*\n*      *\n*      *\n*      *\n********')

def choose():
    nume_jucator = input('Introduceti numele pentru a participa in joc:\n').title()
    suma_bani = int(input('Cu ce suma intrati in concurs?\n'))
    jucator = Player(nume_jucator, suma_bani)
    var1 = Player('Dragos', suma_bani)
    var2 = Player('Razvan', suma_bani)
    var3 = Player('Robert', suma_bani)
    lista_jucatori = [var1, var2, var3, jucator]  # Posibile probleme cand jucatorii se invartesc intre ei si nu mai ocupa aceleasi pozitii in lista.
    return Game(nume_jucator, suma_bani, lista_jucatori) # Aceeasi carte se dubleaza de 2 ori la impartirea mainilor, nu are culoarea diferita


a = choose()
#print(isinstance(, Game))
a.joc_poker()
