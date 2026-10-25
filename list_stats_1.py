'''
List stats 1

Scrivere un programma Python che, data una lista di interi, calcoli e 
scriva a schermo:
 - il valore minimo (ovvero l'intero più piccolo nella lista)
 - il valore massimo
 - il valore medio

Si scriva il programma di modo che:
- non utilizzi alcuna funzione di calcolo di statitistiche offerta 
  da librerie esterne

- scandisca la lista esattamente una volta.


Organizzare il programma in opportune funzioni.
'''

import sys

def input_list():
    user_list = []
    print("Inserisci numeri da aggiungere alla lista oppure lascia l'input vuoto per smettere: ")
    while True:
        numbers_for_list = input()
        if numbers_for_list == "":
            break
        else:
            user_list.append(int(numbers_for_list))
    return user_list

def list_stats(user_list:list[int]):
    massimo = None
    minimo = None
    somma = 0

    for n in user_list:
        if massimo is None or n > massimo: # Verifico se massimo è None (prima iterazione) oppure se n è maggiore di massimo
            massimo = n
        if minimo is None or n < minimo: # Verifico se minimo è None (prima iterazione) oppure se n è minore di minimo
            minimo = n 
        somma += n 
    return (massimo, minimo, somma / len(user_list)) # Restituisco una tupla di valori di ritorno da stampare nel main (le tuple sono con le PARENTESI TONDE!!)
	
def main():
    list_of_int = input_list()
    result = list_stats(list_of_int)
    print(f"Massimo: {result[0]}, Minimo: {result[1]}, Media: {result[2]}") # Richiamo i valori massimo, minimo e media dalla tupla di ritorno della funzione list_stats
    return 0

if __name__ == '__main__':
    sys.exit(main())