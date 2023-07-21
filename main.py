import random

valor_seed = str(input("Digite para quem você quer mandar a mensagem: "))
random.seed(valor_seed)

table1 = {}

for i in range(32, 127):
    char = chr(i)
    binary = bin(i)[2:].zfill(8)
    table1[char] = binary

for j in range(161, 256):
    character = chr(j)
    binaryo = bin(j)[2:].zfill(8)
    table1[character] = binaryo


def check_table(table):
    binary_values = list(table.values())
    duplicates = set([x for x in binary_values if binary_values.count(x) > 1])
    if duplicates:
        print("Números binários repetidos na tabela:")
        for binary in duplicates:
            characters = [char for char, value in table.items() if value == binary]
            print(f"Binary: {binary}, Characters: {characters}")


def criar_tabelas(quantidade):
    Tables = []
    for g in range(quantidade):
        dicionario = {}
        check_table(table1)
        for chave, binario in table1.items():
            num_binario = random.choice(["0", "1"])
            dicionario[chave] = binario + (num_binario)
        table1.update(dicionario)
        Tables.append(dicionario)
    random.shuffle(Tables)
    return Tables


'''num_tabelas = int(input("Quantidade de tabelas:"))'''
num_tabelas = random.randint(8, 20)
Tabels = criar_tabelas(num_tabelas)
#Mostrar as Tabelas
'''for i in range(len(Tabels)):
  for chave, valor in Tabels[i].items():
      print(f"'{chave}': '{valor}'", end=",\n")'''

Chave = {
    "tabelas": Tabels,
}


def encriptografar(Mensagem, Chave):
    contador = 0
    valor_criptografado = ""

    while contador < len(Mensagem):
        for tabela in range(len(Chave["tabelas"])):
            if contador < len(Mensagem):
                caracter = Mensagem[contador]
                if caracter in Chave["tabelas"][tabela].keys():
                    valor_criptografado += Chave["tabelas"][tabela][caracter]
            contador += 1
            if contador >= len(Mensagem):
                break
    return valor_criptografado


def descriptografar(valor_criptografado, chave):
    contador = 0
    mensagem_descriptografada = ""
    encontrado = False

    while contador < len(valor_criptografado):
        for tabela in chave["tabelas"]:
            for caractere, codigo in tabela.items():
                if valor_criptografado.startswith(codigo, contador):
                    mensagem_descriptografada += caractere
                    contador += len(codigo)
                    encontrado = True 
                    break

        if not encontrado:
            return "Chave Incorreta"

        encontrado = False

    return mensagem_descriptografada

def menu():
    while True:
        print("Menu:")
        print("1. Criptografar")
        print("2. Descriptografar")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            Mensagem = str(input("Digite a mensagem que deseja criptografar:"))
            valor_criptografado = encriptografar(Mensagem, Chave)
            print("Valor criptografado:{}".format(valor_criptografado))
            print()
        elif escolha == "2":
            valor_criptografado = input("Digite o valor criptografado:")
            mensagem_descriptografada = descriptografar(valor_criptografado, Chave)
            if mensagem_descriptografada == "Chave Incorreta": 
                print("\n", mensagem_descriptografada, "\n")
            else:
                print("\nMensagem descriptografada:{}".format(mensagem_descriptografada))
                print()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
            print()

menu()