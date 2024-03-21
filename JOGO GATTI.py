import random

def sorteia_alvo():
    return random.randint(1, 20)

def pede_palpite():
    palpite = int(input("Tente adivinhar o número sorteado entre 1 e 20: "))
    return palpite

def verifica_palpite(alvo, palpite):
    if palpite == alvo:
        print("Parabéns! Você acertou o número.")
        return True
    elif palpite < alvo:
        print("Seu palpite está muito baixo. Tente novamente.")
    else:
        print("Seu palpite está muito alto. Tente novamente.")
    return False

def atualiza_alvo(alvo):
    novo_alvo = alvo + sorteia_alvo()
    if novo_alvo < 100:
        print(f"O computador ganhou! O alvo final era {novo_alvo}.")
        return None
    return novo_alvo

def main():
    alvo = sorteia_alvo()
    while True:
        palpite = pede_palpite()
        if verifica_palpite(alvo, palpite):
            break
        alvo = atualiza_alvo(alvo)
        if alvo is None:
            break

if __name__ == "__main__":
    main()