import random

nomes = ['Ana', 'João', ' Maria', 'Pedro', 'Julia', 'Lucas', 'Beatriz', 'Guilherme', 'Isabela', 'Matheus',
         'Sophia', 'Rafael', 'Laura', 'Gabriel', 'Manuela', 'Leonardo', 'Valentina', 'Felipe', 'Luiza Enzo']

sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Almeida", "Pereira", "Gomes", "Costa",
              "Carvalho", "Martins", "Ribeiro", "Lima", "Araújo", "Cruz", "Mendes", "Nascimento", "Fernandes", "Cardoso"]

# Gerar uma idade aleatória entre 16 e 69 anos


def gerar_idade():
    return random.randint(16, 69)

# Função principal para criar o arquivo com N nomes completos e idades aleatórias


def criar_arquivo_com_dados_aleatorios(N, nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as arquivo:
        for _ in range(N):
            nome = random.choice(nomes)
            sobrenome = random.choice(sobrenomes)
            idade = gerar_idade()
            nome_completo = f"{nome} {sobrenome}"
            linha = f"{nome_completo},{idade}\n"
            arquivo.write(linha)


if __name__ == "__main__":
    try:
        N = int(input("Digite o número de nomes e idades a serem gerados: "))
        nome_do_arquivo = input("Digite o nome do arquivo de saída: ")

        criar_arquivo_com_dados_aleatorios(N, nome_do_arquivo)
        print(
            f"{N} nomes completos e idades aleatórias foram gerados e escritos em '{nome_do_arquivo}'.")
    except ValueError:
        print("Por favor, insira um número válido para N.")