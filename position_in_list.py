'''
Position in list

Scrivere un programma che, legge da input:
 - una lista 'l' di stringhe e
 - una singola stringa 's'

e scrive a schermo la posizione di 's' nella lista 'l'.
In partciolare se 's' occorre (ovvero compare) nella lista 'l' scrive:

	f"La stringa {s} occorre in {l} alla posizione ..." 

Se invece 's' non occorre nella lista 'l' scrive:

	f"La stringa {s} non occorre in {l}".


Organizzare il programma in opportune funzioni.

'''

import sys

def get_list_of_strings():
	l = []
	print("Scrivi delle frasi da aggiungere alla lista oppure lascia vuoto per terminare: ")
	while True:
		input_string = input()
		if input_string == "":
			break
		else:
			l.append(input_string)
	return l

def get_string():
	string_to_verify = input("Digita la stringa che vuoi verificare: ")
	return string_to_verify

def position_in_list(l:list[str], s:str):
	result = 0
	for ind in range(len(l)):
		if l[ind] == s:
			result = ind
			return f"la stringa \"{s}\" occorre nella lista {l} alla posizione {result}"
		if s not in l:
			return f"la stringa \"{s}\" non è presente nella lista {l}"

def main():
	user_list_of_strings = get_list_of_strings()
	user_string = get_string()
	print(position_in_list(user_list_of_strings, user_string))


if __name__ == '__main__':
	sys.exit(main())
