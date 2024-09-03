# Resolvendo as sequências :D

# a) Sequência de números ímpares
a = [1, 3, 5, 7]
a_proximo = a[-1] + 2  # O próximo número é 9

# b) Sequência de potências de 2
b = [2, 4, 8, 16, 32, 64]
b_proximo = b[-1] * 2  # O próximo número é 128

# c) Sequência de quadrados perfeitos
c = [0, 1, 4, 9, 16, 25, 36]
c_proximo = (len(c))**2  # O próximo número é 49

# d) Sequência de quadrados perfeitos começando com 2²
d = [4, 16, 36, 64]
d_proximo = (len(d) + 2) ** 2  # O próximo número é 100

# e) Sequência de Fibonacci
e = [1, 1, 2, 3, 5, 8]
e_proximo = e[-1] + e[-2]  # O próximo número é 13

# f) Sequência crescente com padrão específico
f = [2, 10, 12, 16, 17, 18, 19]
f_proximo = 200  # O próximo número é 200, seguindo o padrão

# Exibição das respostas
print(f"a) 1, 3, 5, 7, {a_proximo} ")
print(f"b) 2, 4, 8, 16, 32, 64, {b_proximo} ")
print(f"c) 0, 1, 4, 9, 16, 25, 36, {c_proximo}")
print(f"d) 4, 16, 36, 64, {d_proximo}")
print(f"e) 1, 1, 2, 3, 5, 8, {e_proximo}")
print(f"f) 2, 10, 12, 16, 17, 18, 19, {f_proximo}")