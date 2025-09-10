# Walrus

# Exercicio 1
#inputar idade/ condição >= 18/ armazena idade/ imprime se pode dirigir ou nao e comunica idade armazenada.


if (idade := int(input("Digite sua idade: "))) >= 18:
    print(f"Permitido dirigir! Idade: {idade}")
else:
    print("Não tem idade para dirigir")

# Exercicio 2
# Controle de estoque
# O usuario deve digitar a quantidade de um produto no estoque
# > 50 = estoque cheio, "x" unidades/ entre 1 e 50 = estoque baixo, "x" unidades/ 0 = produto esgotado


if (quantidade_produto := int(input("Digite a quantidade do produto x: "))) > 50:
    print(f"Estoque cheio: {quantidade_produto} unidades")
elif 1 <= quantidade_produto <= 50:
    print(f"estoque baixo: {quantidade_produto} unidades")
else:
    print(f"produto esgotado!!")


# Exercicio 3
# Média de motas
# Peça 3 notas ao usuário (uma por vez)
# Use := para capturar cada nota e ir acumulando a soma
# Calcule a média
# Se a média for:
    # maior ou igual a 7 print aprovado com média x
    # entre 5 e 6,9 print recuperação com media x
    # menor que 5 print reprovado com media x

soma = (nota_1 := float(input("Digite a primeira nota: ")))
soma += (nota_2 := float(input("Digite a segunda nota: ")))
soma += (nota_3 := float(input("Digite a terceira nota: ")))
media_nota = soma / 3

if media_nota >= 7:
    print (f"Aprovado com media: ",{media_nota})
if soma < 30:
    print("Boa sorte!")
elif 5 <= media_nota <= 6.9:
    print (f"Recuperação com media: ",{media_nota})
elif media_nota < 5:
    print (f"Reprovado com média: ",{media_nota})

    # SOLUÇÃO ATUALIZADA

soma = 0.0
qtd = 0
while qtd < 3:
    if 0.0 <= (nota:= float(input(f"Digite a {qtd+1}º nota (0 a 10): "))) <= 10:
        soma += nota
        qtd += 1
    else:
        print("Nota inválida, use valores entre 0 e 10.")
media = soma / 3
if media >= 7:
    print(f"Aprovado com média: {media:.2f}")
elif media >= 5:
    print(f"De recuperação com media: {media:.2f}")
else:
    print(f"Reprovado com media: {media:.2f}")


# Exercicio 4
# Caixa eletrônico
# Peça ao usuário o valor que deseja sacar
# Se o valor for maior que zero e múltiplo de 10 permita o saque
# Caso contrário mostre valor inválido
# Use o Walrus na condição e calcule tambem quantas notas de 50, 20 e 10 seriam entregues


saque = int(input("Qual o valor do saque? "))
notas_50 = saque // 50
resto_50 = saque % 50

notas_20 = resto_50 // 20
resto_20 = resto_50 % 20

notas_10 = resto_20 // 10
resto_10 = resto_20 % 10

if saque >= 50 :
    print(f"Você vai receber: {notas_50} notas de 50")
if 20 <= resto_50 <= 40:
    print(f"Você vai receber: {notas_20} notas de 20")
if 0 <= resto_20 <= 10:
    print(f"Você vai receber: {notas_10} notas 10")
else:
    print("Saque não permitido")

    # SOLUÇÃO ATUALIZADA
# Não calcular nada se o valor for inválido
# Mensagem clara para zero, negativos e não múltiplos de 10
# Contar notas com divmod (mais elegante que \\ e % separados)
# Nao imprimir denominaçoes com quantidade 0

# Lê e valida numa tacada só com walrus
if not ((valor:= int(input("Valor do saque (múltiplo de 10): ")))) > 0 and valor % 10 == 0:
    print("Erro! Saque inválido: informe um inteiro positivo múltiplo de 10 (ex: 10, 20, 50, 130)")
else:
    nota = {}

    qtd50, resto = divmod(valor, 50)
    if qtd50: notas[50] = qtd50

    qtd20, resto = divmod(valor, 20)
    if qtd20: notas[20] = qtd20

    qtd10, resto = divmod(valor, 10)
    if qtd10: notas[10] = qtd10
# resto aqui será sempre zero por causa da validação
partes = [f"{qtd}x{nota}" for nota, qtd in notas.items()]
print("Saque permitido! Notas:", ", ".join(partes))

# DESAFIO
# Nesse código há um erro, bem simples até. Descubra e me mande uma menasagem







