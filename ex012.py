num = int(input('Digite um numero inteiro e descubra seu fatorial: '))


resultado = 1
count = 1

while count <= num:
    resultado *= count
    print('{} -> '.format(count), end='')
    count += 1


print(resultado)
