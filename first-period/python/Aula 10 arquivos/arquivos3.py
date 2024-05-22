def arquivo_copiar(arquivo_source, arquivo_destination):
    try:
        with open(arquivo_source, 'r') as source, open(arquivo_destination, 'w') as destination:
            for linha in source:
                #verificar se a linha não é um comentário (não começa com #)
                if not linha.strip().startswith('#'):
                    destination.write(linha)
        print(f"Conteúdo do arquivo '{arquivo_source}' copiado para '{arquivo_destination}' (ignorando comentários).")
    except FileNotFoundError:
        print(f"O arquivo '{arquivo_source}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao copiar o arquivo: {str(e)}")

if __name__ == "__main__":
    arquivo_source = input("Digite o nome do arquivo de origem: ")
    arquivo_destination = input("Digite o nome do arquivo de destino: ")

    arquivo_copiar(arquivo_source, arquivo_destination)