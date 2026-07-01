import sys

def input_string():
    stringa_da_verificare = input("Scrivi una frase e ti dirò se è palindroma o meno: ")
    return stringa_da_verificare

def string_cleaner(stringa:str):
    # stringa_pulita = ""
    # for c in stringa:
    #     if c != " ":
    #         stringa_pulita += c
    # return stringa_pulita.lower()
    return stringa.replace(" ", "").lower()


def is_palyndrome(stringa):
    if stringa == stringa[::-1]:
        return True
    return False

def main():
    stringa_da_verificare = string_cleaner(input_string())
    print(f"La stringa {stringa_da_verificare} è palindroma?", is_palyndrome(stringa_da_verificare))

if __name__ == "__main__":
    sys.exit(main())