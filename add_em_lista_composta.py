galera = []
temp = []

# Crio uma lista temporária, para criar uma lista a cada laço de repetição, e inserir essa lista temporária na lista final.
# A cada iteração no range, eu crio uma lista, e penduro essa lista na lista final (em formato de lista).

for c in range(3):
    temp.append(str(input('Digite o nome: ')))
    temp.append(int(input('Digite a idade: ')))
    galera.append(temp[:])
    print(temp)
    temp.clear() # limpo o dado temporário, senão ela vai adicionar

print(galera)

# Ex: para exibir quem tem idade +18 e quem tem menos:
for pes in galera:
    if pes[1] >= 18:
        print(f'{pes[0]} tem {pes[1]} e é maior de idade.')
    else:
        print(f'{pes[0]} tem {pes[1]} e é menor de idade')
