'''
Initial substring

Scrivere un programma Python che, date due stringhe, string e accept, 
scriva a schermo la porzione iniziale più lunga di string che contiene 
solo caratteri che occorrono in accept.
Ad esempio, con string = "ciao mondo" e accept = "moia oc", 
il programma deve scrivere a schermo "ciao mo".

Successivamente, modificare il programma di modo che:
 - definisca una opportuna funzione 
	   initial_substring(string:str, accept:str)->str 
   che effettua il calcolo e restituisce il risultato
 - prenda l'input dell'utente (i valori per string e accept) da tastiera, 
   invochi la funzione e ne stampi il risultato a schermo.
'''

import sys


def initial_substring(string:str, accept:str)->str:
	final_string = ""
	for c in string:
		if c in accept:
			final_string += c 
	return final_string

def main():
	string = input("String: ")
	accept = input("Accept: ")
	print("la sottostringa è", initial_substring(string, accept))
	return 0

if __name__ == '__main__':
	sys.exit(main())
