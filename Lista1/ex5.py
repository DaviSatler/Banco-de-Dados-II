a = int(input('Me fale um número para ser o numerador: '))
b = int(input('Me fale outro número para ser o denominador: '))

if b == 0:
    print('Denominador não pode ser ZERO!')
else:
    div = a // b
    print(f'O resultado dos dois números são: {div}')
