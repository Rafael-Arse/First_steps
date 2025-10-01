# loop/ soma numeros e me fala quem é o menor/ maior numero

cont = 1
soma = 0
maior_valor = 0
menor_valor =0
while cont <= 5:
    valor = int(input("Digite o numero a ser somado:"))
    if valor > maior_valor:
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor
    soma += valor
    cont += 1
print(f"A soma dos valores é {soma}")
print(f"O maior numero é {maior_valor}")
print(f"O menor numero é {menor_valor}")

# Conversor de moedas com loop

qtd = int(input("Quantas vezes vc quer converter? "))
cont = 1
total = 0
total_dolar = 0
while cont <= qtd:
    valor = float(input("Qual o valor em dolar? $"))
    cont += 1
    reais = valor * 5
    total = total + reais
    total_dolar = total_dolar + valor
    print(f"conversao do valor: {reais:.2f}R$")
print(f"conversao total {total:.2f}R$")
print(f"valor em dolar {total_dolar:.2f}$")

# Contagem crescente e decrescente com condicao

inicio = int(input("Inicio da contagem: "))
final = int(input("final da contagem: "))

if inicio < final:
    while inicio <= final:
        print(inicio)
        inicio += 1

elif inicio > final:
    while inicio >= final:
        print (inicio)
        inicio -= 1

else:
    print("Valores iguais, nao existe contagem")

"""
    recebe quantidade de alunos
    recebe nome e nota do aluno
    se nota do aluno 1 é maior que aluno 2, printa 'melhor aproveitamento' do aluno 1
    passa essa condicao durante o loop para todas as notas
    printa o melhor ou melhores alunos se algumas notas forem iguais

"""



# Comparar nota de alunos/ min 2 alunos para comparacao

qtd = int(input("Quantos alunos tem dentro da turma? "))

if qtd :
    cont = 0
    nota_maior = 0
    melhores_alunos = []
    while cont < qtd:
        nome = input("digite o nome do aluno: ")
        nota = float(input("digite a nota do aluno: "))
        cont += 1
        if nota > nota_maior:
            nota_maior = nota
            melhores_alunos = [(nome, nota)]
        elif nota == nota_maior:
            melhores_alunos.append((nome, nota))

print ("O(s) aluno(s) com maior aproveitamento:")
for aluno, nota in melhores_alunos:
    print(f"{aluno} com nota {nota}")

# Contagem regressiva de uma lista de numeros definida pelo usuario

numeros = list(map(int, input("Digite numeros separados por vírgula para contagem: ").split(",")))

for num in numeros:
    print(f"Contagem regressiva a partir do numero {num}:")
    while num > 0:
        print(num)
        num -= 1


# XXXXXXXXXXX RESOLVER PROBLEMA DE ADICIONAR NUMEROS A UMA LISTA XXXXXXXXXXXX

lista = [int(x.replace(" ", ",")) for x in input("Adicionando valores em lista: ")]
print(lista)



entrada = input("Adicionando valores em lista: ")
numeros = [int(x) for x in entrada.replace(","," ").strip()]
lista = []
i = 0
while i < len(numeros):
    i += 1
    lista.append(numeros[i])
print(lista)


# FATORIAL

num = int(input("Qual o fatorial a ser calculado? "))
acum_result = 1
cont = num
while cont > 0:
        acum_result *= cont
        cont -= 1
print(f"Fatorial de {num} é {acum_result}")

# FATORIAL ATÉ PEDIR PRA PARAR

while True:
    num = int(input("Qual o fatorial a ser calculado? "))
    acum_result = 1
    cont = num
    while cont > 0:
        acum_result *= cont
        cont -= 1
    print(f"O fatorial de {num} é {acum_result}")

    continuar = input("Deseja continuar? (s ou n): ").strip().lower()
    if continuar != "s":
        break

# DESCOBRIR SE UM NUMERO É PRIMO OU NAO

num = int(input("Digite um numero: "))
cont = 0
cont_div = 0
while cont < num:
    cont += 1
    if num % cont == 0:
        cont_div += 1
if cont_div > 2:
    print("O numero não é primo")
else:
    print("O numero é primo")


# MENU DE OPCOES PARA, CONT (CRESCENTE/ DECRESCENTE/ SAIR)

print("================")
print("|     MENU     |")
print("================")
print("| [1] DE 1 A 10| ")
print("| [2] DE 10 A 1| ")
print("| [3] Sair     | ")
print("================")

entrada = int(input("Escolha 1 das 3 opçoes: "))
cont_plus = 0
cont_less = 11
while cont_plus < 10:
    cont_plus += 1
    if entrada == 1:
        print(cont_plus)
while cont_less > 1:
    cont_less -= 1
    if entrada == 2:
        print(cont_less)
    else:
        print("Encerrando")


# PROGRAMA QUE PEDE O SEXO/ IDADE/ COR DO CABELO ONDE:
# O PROGRAMA TE DÁ AS OPCOES DE COR DE CABELO PARA SELECIONAR UMA: 1/PRETO, 2/CASTANHO, 3/LOIRO, 4/RUIVO
# AO FINAL PERGUNTA SE QUER CONTINUAR (S/N)

print("======================")
print("  SELETOR DE PESSOAS  ")
print("======================")

homens_castanhos = 0
mulheres_loiras = 0
continuar = True
while continuar:
    sexo = input("Qual o sexo? (h/m) ").strip().lower()
    if sexo not in ("h", "m"):
        print("Sexo inválido")
        continuar = input("Quer continuar? (s/n) ").strip().lower()
        if continuar == "n":   # ESTÁ TUDO OK SEYCU, POREM NESTA PARTE DO CÓDIGO MINHA CONDIÇAO SEMPRE DA TRUE
            print("Encerrando")# MESMO COLOCANDO "n", TENTEI COLOCAR ATÉ "continuar = False" APÓS O IF MAS NAO RESOLVEU
            break
        else:
            continue

    idade = int(input("Qual a idade? "))
    if not idade < 16:
        print("Somente Homens ou mulheres a partir dos 16: ")
        continuar = input("Quer continuar? (s/n) ").strip().lower()
        if continuar == "n":
            print("Encerrando")
            break
        else:
            continue

    cor_cabelo = int(input("Qual a cor do cabelo? [1] Preto, [2] Castanho, [3] Loiro, [4] Ruivo "))
    match cor_cabelo:
        case 1:
            cor_cabelo = "Preto"
        case 2:
            cor_cabelo = "Castanho"
        case 3:
            cor_cabelo = "Loiro"
        case 4:
            cor_cabelo = "Ruivo"
        case _:
            print("Digite um numero entre 1 e 4 ")
            continuar = input("Quer continuar? (s/n) ").strip().lower()
            if continuar == "n":
                print("Encerrando")
                break
            else:
                continue


    if sexo == "h" and idade > 18 and cor_cabelo == "Castanho":
        homens_castanhos += 1
    if sexo == "m" and 25 <= idade <= 30 and cor_cabelo == "Loiro":
        mulheres_loiras += 1
    continuar = input("Quer continuar? (s/n) ").strip().lower()

    if continuar == "n":
        print("fim do seletor")
        break

print(f"Total de homens com mais de 18 e cabelos castanhos: {homens_castanhos}")
print(f"Total de mulheres entre 25 e 30 e cabelos loiros: {mulheres_loiras}")

# ESTRUTURA COND. FOR

# Forma do range: range(inicio, fim, passo), Inicio padrao 0/ nao inclui o valor final/ passo é dequanto em quanto, padrao 1
# Contagem de 1 a 10
for num in range(0, 11):
    print(num)

# Range para listas/ tuplas
Almoco = ["Arroz", "Feijao", "Carne"]
for i in range(len(Almoco)):
    print(i, Almoco[i])

# Converter sequencia em listas/ tuplas
print(list(range(8)))

# Somatório dos numeros de 1 a 100
soma = 0
for num in range(1, 101):
    soma += num
print(soma)

# Contar quantos numeros existem em uma sequencia estabelecida

valores = []
for num in range(1, 6):
    valor = int(input("Digite até 5 numeros "))

    if 1 <= valor <= 100:
        valores.append(valor)
    cond = input("Deseja digitar outro valor?(s/n) ").strip().lower()
    if cond != "n":
        continue
    else:
        break

print(f"Os numeros {valores} estão entre 1 e 100, {len(valores)} numeros ")

# Analise combinatoria/ fazer todas as combinaçoes entre 1, 2, 3 para 2 colunas

for c1 in range(1, 4):
    for c2 in range(1, 4):
        print(c1, c2)

# An. Comb/ combinando produtos em lista

produtos = ["Arroz", "Feijão", "Carne", "Macarrão"]

for i in range(len(produtos)):
    for j in range(len(produtos)):
        if i != j:   # evitar combinacoes repetidas # p/ (if j > i:) só pega quando o segundo vem depois do primeiro, evita mesma combinaçao mas com ordem trocada
            print(produtos[i], "-", produtos[j])


# FiBONACCI

f = [0, 1]
for _ in range(2, 16):
    prox_num = f[-1] + f[-2]
    f.append(prox_num)

print(f)

# FiBONACCI MAIS PURO

a, b = 0, 1
for _ in range(16):
    print(a)
    a, b = b, a + b

print(a)

# Analisador de valores: Soma/ Média/ Div 5/ Nulos/ Sum. Pares
soma = 0
div_5 = 0
nulo = 0
soma_pares = 0
qtd = []
for n in range(1000):
    var = int(input("Digite um valor: "))
    qtd.append(var)

    soma += var
    media = soma / len(qtd)          
    
    if var % 5 == 0:
        div_5 += 1
    if var == 0:
        nulo += 1
    if var % 2 == 0:
        soma_pares += var

    condicao = input("Deseja continuar? (s/n) ").strip().lower()
    if condicao == "n":
        break
    else:
        continue

print(f"A soma de todos os valores é: {soma}")
print(f"A media de todos os valores é: {media}")
print(f"Há {div_5} valores divisiveis por 5")
print(f"Há {nulo} valores nulos ") 
print(f"A soma de todos os valores pares é: {soma_pares}")








