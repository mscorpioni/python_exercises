num = int(input('Digite um número: '))

total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\nO número {num} foi divisível {total} vezes', end=' ')
if total == 2:
    print('e por isso É PRIMO.')
else:
    print('e por isso NÃO É PRIMO')