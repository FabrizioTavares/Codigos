import RandomListGen


def counting_sort(lista, maior_valor):
    m = maior_valor + 1
    contagem = [0] * m
    for a in lista:
        # contar ocorrencias
        contagem[a] += 1
    i = 0
    for a in range(m):
        for c in range(contagem[a]):
            lista[i] = a
            i += 1
    return lista


xx = RandomListGen.generate(60000, 1, 10)

print(xx)
print(counting_sort(xx, 10))
