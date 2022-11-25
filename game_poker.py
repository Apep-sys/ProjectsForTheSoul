import random
from player_poker import Player


class Game(Player):
    """var1 = Player('Dragos', 500)
    var2 = Player('Razvan', 500)
    var3 = Player('Robert', 500)
    lista_jucatori = [var1, var2, var3"""
    jucator_principal = None
    lista_jucatori = None
    lista_pariu = [0, 2, 5, 10, 50, 100]
    lista_carti = []
    table_cards = [] # Table cards va trebui sa preia valoarea
                     # listei de carti ramase de la player ( ex. 44 carti ramase )
                     # deci table_cards va alege doar din alea 44 de carti

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
                Game.lista_carti = y[1] # 1 reprezinta indicele pentru lista de carti ramasa
                                        # 0 reprezinta indicele pentru cartile alese
            for x in Game.lista_jucatori:
                print(x.mana_carti, x.nume_jucator)
            print('Mana dvs. este:', Game.lista_jucatori[3].mana_carti)
        '''print('Acum pariati!')
        for x in self.lista_jucatori:
            x.bet'''
        if x == 1:
            print('\nDealerul va da acum prima serie- Flop!')
            print('Cartile sunt:')
            y = Game.alegere_carti(self, 0, Game.lista_carti)
            Game.table_cards = y[0]
            Game.lista_carti = y[1]
            print(Game.table_cards)
            #print(list(Game.table_cards[0][0].values())[0])
        if x == 2:
            print('\nDealerul va da acum a doua serie- Turn!')
            y = Game.alegere_carti(self, 2, Game.lista_carti)
            Game.table_cards = y[0]
            Game.lista_carti = y[1]
            '''while True:
                try:
                    if y in temporary_cards:
                        continue
                except:
                    pass'''
            #Game.table_cards.append(y)
            print(Game.table_cards)
        if x == 3:
            print('\nDealerul va da acum ultima serie- River!')
            y = Game.alegere_carti(self, 2, Game.lista_carti)
            Game.table_cards = y[0]
            Game.lista_carti = y[1]
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
        #small_blind[0] e ultima suma si big_b[0] e ultimul bet
        lista_temporara = Game.lista_jucatori[2:4]
        for turn in lista_temporara:
            pariu_runda_0 = pariu_mare
            if turn.nume_jucator == Game.jucator_principal.nume_jucator:
                print(f'Pariati {pariu_mare} sau mai mult pentru a intra in joc.\nBani ramasi: {self.suma_bani}')
                while True:
                    pariu_introdus = int(input())
                    if pariu_introdus < pariu_runda_0:
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
                suma_calculata = turn.bet(Game.lista_pariu[1], suma_actuala, pariu_mare, 0)
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

    def hand_ranking(self, mana_carti, table_cards, i):
        self.mana_carti = mana_carti
        Game.table_cards = table_cards
        lista_straight = []
        lista_flush = []
        #print(Game.jucator_principal.mana_carti)
        straight1 = ['10', 'A', 'J', 'Q', 'K']
        royal_Flush = 0
        straight_Flush = 0
        four_Kind = 0
        full_House = 0
        flush = 0
        straight = 0
        three_Kind = 0
        two_pair = 0
        pair = 0
        high_Card = 0
        # Verificam daca se potrivesc valorile cartilor
        for x in mana_carti.keys():
            if x == '10':
                for y in table_cards.keys(): # De dat continue cand se modifica valori gen straight, fullhouse etc.
                    if x[:2] == y[:2]:
                        if x[0] == y[0]:
                            pair += 1
                            if pair == 2:
                                two_pair = pair
                            elif pair == 3:
                                three_Kind = pair
                            elif pair == 4:
                                four_Kind = pair
                    try:
                        if int(y) in range(6, 10):
                            straight += 1
                            # Straight trebuie sa fie 5
                    except:
                        pass
            else:
                for y in table_cards.keys():
                    if x[0] == y[0]:
                        pair += 1
                        if pair == 2:
                            two_pair = pair
                        elif pair == 3:
                            three_Kind = pair
                        elif pair == 4:
                            four_Kind = pair
                    try:
                        if int(x[0]) in range(2, 10):
                            lista_straight.append(x[0])
                            if int(y[0]) in range(2, 10):
                                lista_straight.append(y[0])
                            lista_straight = [int(x) for x in lista_straight]
                            lista_straight.sort()
                            lista_straight = [str(x) for x in lista_straight]
                            for nr in range(len(lista_straight)):
                                if lista_straight[nr] != lista_straight[len(lista_straight) - 1]:
                                    if (lista_straight[nr + 1] - lista_straight[nr]) == 1:
                                        straight += 1
                                # Straight trebuie sa fie 5
                    except:
                        pass
                    if x[0] in straight1:
                        if y[0] in straight1:
                            royal_Flush += 1
                            # Royal Flush trebuie sa fie 5

        # Verificam daca se potrivesc culorile cartilor:
        for x in mana_carti.values():
            flush = 0
            for y in table_cards.values():
                if x == y:
                    flush += 1
                    # Flush trebuie sa fie 5



        # Verificam combinatii de maini:
        if flush == 5 and straight == 5:
            print(f'Aveti un Straight Flush! {i.nume_jucator, i.mana_carti}')
        if flush == 5 and straight < 5:
            print(f'Aveti un Flush! {i.nume_jucator, i.mana_carti}')
        if straight == 5 and flush < 5:
            print(f'Aveti un Straight! {i.nume_jucator, i.mana_carti}')
        if pair == 1 and two_pair == 0 and three_Kind == 0 and four_Kind == 0:
            print(f'Aveti o pereche! {i.nume_jucator, i.mana_carti}')
        if two_pair and  pair == 0 and three_Kind == 0 and four_Kind == 0== 2:
            print(f'Aveti doua perechi! {i.nume_jucator, i.mana_carti}')
        if three_Kind == 3 and two_pair == 0 and pair == 0 and four_Kind == 0:
            print(f'Aveti un triplet! {i.nume_jucator, i.mana_carti}')
        if four_Kind == 4 and two_pair == 0 and three_Kind == 0 and pair == 0:
            print(f'Aveti un cvartet! {i.nume_jucator, i.mana_carti}')
        if flush == 5 and royal_Flush == 5:
            print(f'Aveti un Royal Flush! {i.nume_jucator, i.mana_carti}')
        if two_pair == 2 and three_Kind == 3:
            print(f'Aveti un Full House! {i.nume_jucator, i.mana_carti}')



    def joc_poker(self):
        suma_actuala = 0
        print('Bine ati venit la Campionatul Saptamanal de Poker!')
        print(f'Jucatorii din aceasta seara sunt {self.lista_jucatori[0].nume_jucator}, '
              f'{self.lista_jucatori[1].nume_jucator}, '
              f'{self.lista_jucatori[2].nume_jucator}, {self.lista_jucatori[3].nume_jucator}')
        print(self.lista_jucatori)
        for i in range(0, 5):
            if i == 0:
                suma_actuala = self.runda0(suma_actuala)
                game_start = self.dealing(0)
                print('\nAcum pariati!')
            else:
                print('Suma actuala: ', suma_actuala)
                suma_actuala = self.runde_shuffle(suma_actuala)
                game_continue = self.dealing(i)
        for i in Game.lista_jucatori:
            Game.hand_ranking(self, i.mana_carti, Game.table_cards, i)

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
    return Game(nume_jucator, suma_bani, lista_jucatori)


a = choose()
#print(isinstance(, Game))
a.joc_poker()