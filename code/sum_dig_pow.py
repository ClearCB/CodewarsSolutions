def sum_dig_pow(a,b):
    resultado = []
    for i in range (a,b+1):
        indice = 1
        numero = str(i)
        suma = 0
        for j in numero:
            cifra = int(j)
            suma += cifra**indice
            indice += 1
            if suma == i:
                resultado.append(i)
            else:
                continue
    return resultado





if __name__ == "__main__":
    print("Testing")
    assert sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
    assert sum_dig_pow(10, 89)  == [89]
    assert sum_dig_pow(10, 100) == [89]
    assert sum_dig_pow(90, 100)  == []
    assert sum_dig_pow(89, 135) == [89, 135]
    print("Passed")