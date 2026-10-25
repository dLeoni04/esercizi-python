'''
List reverse

Scrivere un programma Python che prende in input una lista di interi e calcoli e 
scriva a schermo la lista con gli stessi elementi in ordine inverso.

Ad esempio, ricevuta in input la lista [3, 7, 1], il programma deve 
calcolare [1, 7, 3].
 
Si scriva il programma utilizzando solo i costrutti base del linguaggio,
senza l'ausilio di funzioni offerte da librerie.

Organizzare il programma in opportune funzioni.
'''

import sys

def int_list():
    user_list = []
    print("Inserisci numeri da aggiungere alla lista oppure lascia l'input vuoto per smettere: ")
    while True:
        numbers_for_list = input()
        if numbers_for_list == "":
            break
        else:
            user_list.append(int(numbers_for_list))
    return user_list

def list_reverse(user_list):
    rev_list = user_list[::-1]
    return rev_list

def main():
    numbers_list = int_list()
    print(f"La lista {numbers_list} al contrario è {list_reverse(numbers_list)}")

if __name__ == '__main__':
    sys.exit(main())
