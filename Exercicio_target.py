# Exercicio 1

INDICE = 13
SOMA = 0
K = 0 

while K < INDICE:
    K+= 1
    SOMA += K

print(SOMA)

# Exercicio 2

def fibonacci(N):
    a, b = 0, 1
    while b < N:
        a, b = b, a + b
    return b == N or N == 0

def verificar_numero(numero):
    pertence = fibonacci(numero)
    if pertence:
        return f"O número {numero} pertence à sequência de Fibonacci"
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci"

numero_informado = int(input("Informe um número: "))
resultado = verificar_numero(numero_informado)
print(resultado)

#Exercicio 3

import json
dados_json = '''
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]
'''

dados = json.loads(dados_json)
valores = [item['valor'] for item in dados if item['valor'] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)
print ("O menor faturamento do mês foi de {}".format(menor_valor))
print("O maior faturamento do mês foi de {}".format(maior_valor))
print("A quantidade de dias acima da media do mês foi de {}".format(dias_acima_da_media))

#Exercicio 4

SP = 67.836
RJ = 36.678
MG = 29.229
ES  = 27.165
Outros = 19.849
Soma = (SP + RJ + MG + ES + Outros)

print("{}:{:.0f}%".format("SP",100 * ( SP / Soma)))
print("{}:{:.0f}%".format("RJ",100 * ( RJ / Soma)))
print("{}:{:.0f}%".format("MG",100 * ( MG / Soma)))
print("{}:{:.0f}%".format("ES",100 * ( ES / Soma)))
print("{}:{:.0f}%".format("Outros",100 * ( Outros / Soma)))

#Exercicio 5

string = input("Digite a string que deseja inverter: ")

string_invertida = ""
for caractere in string:
    string_invertida = caractere + string_invertida

print("String invertida:", string_invertida)