def verificar_letra_a(string):
    contador = string.lower().count('a')
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

string = input("Informe uma string: ")
verificar_letra_a(string)