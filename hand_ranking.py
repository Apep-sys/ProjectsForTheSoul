def hand_ranking(mana_carti, table_cards, i):
    lista_straight = []
    lista_flush = []
    # print(Game.jucator_principal.mana_carti)
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
    rankings = [royal_Flush, straight_Flush, four_Kind, full_House, flush, straight, three_Kind, two_pair, pair,
                high_Card]

    # Initializam lista de counter pentru fiecare carte existenta in mana
    chei_duble = list(mana_carti.keys())
    chei_duble = [x[0] for x in chei_duble]
    if chei_duble.count(chei_duble[0]) == 2:
        counter_perechi = {x: 2 for x in mana_carti}
    else:
        counter_perechi = {x: 0 for x in mana_carti}

    # Verificam daca se potrivesc valorile cartilor
    for x in mana_carti.keys():
        lista_straight = []
        if x == '10':
            for y in table_cards.keys():  # De dat continue cand se modifica valori gen straight, fullhouse etc.
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
            for y in table_cards.keys():              # Incrementam counter-ul perechilor
                if x[0] == y[0]:
                    counter_perechi[x] += 1

                # Codul pentru cazul Straight
                try:                                  # Folosim try pentru ca A, K, etc. nu pot fi facute int
                    if int(x[0]) in range(2, 10) and x[0] not in lista_straight and len(lista_straight) != 5:
                        lista_straight.append(x[0])    # Lista cu numere intre 2-10 pentru a testa cazul straight
                    if int(y[0]) in range(2, 10) and len(lista_straight) != 5:
                        lista_straight.append(y[0])
                    if len(lista_straight) == 5:
                        lista_straight = [int(x) for x in lista_straight]
                        lista_straight.sort()
                        consecutiv = True              # Contor pt a vedea daca avem nr consecutive
                        for count, value in enumerate(lista_straight):
                            if value != lista_straight[len(lista_straight) - 1]:   # Nu verificam ultimul element
                                if value == lista_straight[count + 1] - 1:
                                    continue
                                else:
                                    consecutiv = False
                                    break
                        if consecutiv == True:      # Daca ramane True, stim ca valoarea nu s-a modificat de la nr
                            straight = 5            # neconsecutive
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

    # Pentru perechi:
    if list(counter_perechi.values()).count(1) == 2:
        pair = 2
    elif list(counter_perechi.values()).count(2) == 1:
        pair = 3
    elif list(counter_perechi.values()).count(4) == 2:
        pair = 4
    else:
        pair = 1
    print(list(counter_perechi.values()).count(list(counter_perechi.values())[0]))
    print(list(counter_perechi.values()))
    if pair == 1:
        print(f'Aveti o pereche! {i, mana_carti}')
    if pair == 2:
        print(f'Aveti doua perechi! {i, mana_carti}')
    if pair == 3:
        print(f'Aveti un triplet! {i, mana_carti}')
    if pair == 4:
        print(f'Aveti un cvartet! {i, mana_carti}') #Cvartetul nu merge din cauza ca se repeta cheile la dictionar...

    # Pentru straight:

    if flush == 5 and straight == 5:
        print(f'Aveti un Straight Flush! {i, mana_carti}')
    if flush == 5 and straight < 5:
        print(f'Aveti un Flush! {i, mana_carti}')
    if straight == 5:
        print(f'Aveti un Straight! {i, mana_carti}')
    if two_pair and pair == 0 and three_Kind == 0 and four_Kind == 0 == 2:
        print(f'Aveti doua perechi! {i, mana_carti}')
    if three_Kind == 3 and two_pair == 0 and pair == 0 and four_Kind == 0:
        print(f'Aveti un triplet! {i, mana_carti}')
    if four_Kind == 4 and two_pair == 0 and three_Kind == 0 and pair == 0:
        print(f'Aveti un cvartet! {i, mana_carti}')
    if flush == 5 and royal_Flush == 5:
        print(f'Aveti un Royal Flush! {i, mana_carti}')
    if two_pair == 2 and three_Kind == 3:
        print(f'Aveti un Full House! {i, mana_carti}')


pair = {'3':'mama', '32':'tata'}
flush = {'da':'nu', 'yoo':'nu', 'ma':'nu', 'ra':'nu', 'si':'nu'}
straight = {'4':'a', '5':'nu', '6':'yas', '8':'s'}
pair1 = {'3':'mama', '31':'tata'}
royal = {'A':'as','Q':'as','K':'as','J':'as','B':'as'}
hand_ranking(pair, pair1, 'da')