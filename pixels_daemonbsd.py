import webbrowser
import random

# Carrega a blacklist do arquivo
blacklist = []
with open("blacklist.txt", "r") as f:
    for line in f:
        blacklist.append(line.strip())

# Lista para armazenar os números já abertos
numeros_abertos = []

# Pergunta ao usuário quais lands adicionar à blacklist
blacklist_perguntada = False

# Loop para abrir 5000 links
for i in range(1, 5001):
    # Gera um número aleatório entre 1 e 5000
    numero = random.randint(1, 5000)

    # Verifica se o número já foi aberto
    if numero in numeros_abertos:
        continue

    # Verifica se o usuário apertou uma tecla
    if i % 10 == 0:
        input("Aperte qualquer tecla para abrir os próximos 10 links...")

        # Pergunta ao usuário por IDs para blacklist
        if not blacklist_perguntada:
            lands_blacklist = input("Digite os IDs das lands para adicionar à blacklist (separados por vírgula): ")
            lands_blacklist = lands_blacklist.split(",")
            #blacklist_perguntada = True

            # Verifica se o ID da land já está na blacklist
            for land_id in lands_blacklist:
                if land_id in blacklist:
                    print(f"O ID {land_id} já está na blacklist.")
                    continue

            # Adiciona os novos IDs à blacklist
            blacklist += lands_blacklist

            # Salva a blacklist no arquivo
            with open("blacklist.txt", "w") as f:
                for land_id in blacklist:
                    f.write(land_id.strip() + "\n")

    # Verifica se o número está na blacklist
    if numero in blacklist:
        continue

    # Adiciona o número à lista de números abertos
    numeros_abertos.append(numero)

    # Abre o link
    webbrowser.open(f"https://play.pixels.xyz/pixels/share/{numero}")

# Mensagem de finalização
print("Todos os links foram abertos!")