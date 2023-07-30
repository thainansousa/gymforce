def calcularDiaDaSemana(dia):
    if dia == 0:
        return 'SEG'
    elif dia == 1:
        return 'TER'
    elif dia == 2:
        return 'QUA'
    elif dia == 3:
        return 'QUI'
    elif dia == 4:
        return 'SEX'
    elif dia == 5:
        return 'SAB'
    elif dia == 6:
        return 'DOM'
    else:
        return 'Parâmetro incorreto!'