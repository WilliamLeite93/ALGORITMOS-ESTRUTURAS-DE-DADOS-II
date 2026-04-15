temperaturas = [20, 19, 18, 18, 17, 18, 20, 22, 25, 27, 28, 30, 31, 32, 32, 31, 29, 27, 25, 23, 22, 21, 21, 20]

def buscarHora(temperaturas, hora):
    return temperaturas[hora]

hora = 1
resultado = buscarHora(temperaturas, hora)

print('Busca de temperatura por hora:')
print(f'A temperatura ás {hora}:00 é de {resultado}°C')


def existeTemperatura(temperaturas, valorBuscado):
    for i in range(len(temperaturas)):
        if temperaturas[i] == valorBuscado:
            return i
    return -1

valorBuscado = 25
resultado = existeTemperatura(temperaturas, valorBuscado)

print()
print('Busca por indíce da temperatura:')
print(f'O primeiro índice da temperatura {valorBuscado}°C é o índice {resultado}')

def buscaExtremos(temperaturas):
    valorMaior = temperaturas[0]
    valorMenor = temperaturas[0]
    for i in range(1, len(temperaturas)):
        if temperaturas[i] > valorMaior:
            valorMaior = temperaturas[i]
        if temperaturas[i] < valorMenor:
            valorMenor = temperaturas[i]
    return valorMaior, valorMenor

temperatura_max, temperatura_min = buscaExtremos(temperaturas)

print()
print(f'A maior temperatura é {temperatura_max}°C')
print(f'A menor temperatura é {temperatura_min}°C')