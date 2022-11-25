from game_poker import Game

def runda0(self, suma_actuala):
    global pariu_introdus
    big_blind = 2
    small_blind = 1
    pariu_mare = big_blind  # Cazul in care abia a inceput runda si s-au dat cartile!
    big_b = Game.lista_jucatori[0].bet(big_blind, suma_actuala, big_blind, 0)
    small_b = Game.lista_jucatori[1].bet(small_blind, big_b[0], pariu_mare, 0)
    suma_actuala = small_b[0]
    # bb[0] e noua suma si bb[1] ultimul bet
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
                            suma_calculata = jucator.bet(
                                jucator.suma_bani - (Game.jucator_principal.suma_bani - pariu_introdus), suma_actuala,
                                pariu_introdus, 0)
                            suma_actuala = suma_calculata[0]
                break
        else:
            suma_calculata = turn.bet(Game.lista_pariu[0], suma_actuala, pariu_mare, 0)
            suma_actuala = suma_calculata[0]
    # suma_calculata = Game.lista_jucatori[1].bet(1, suma_actuala, pariu_mare, 0)
    # suma_actuala = suma_calculata[0]
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
        # y = self.bet(pariu, small_b[0], small_b[1], runda)[0]
        ### DE CONTINUAT! Grija daca exista un pariu inainte sau nu.
    '''print(turn)
    x = self.lista_jucatori[turn]
    self.lista_jucatori[turn] = self.lista_jucatori[turn + 1]
    self.lista_jucatori[3] = x'''
    return suma_actuala