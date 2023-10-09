def calcular_media(notas):
    notas = [float(nota) for nota in notas]  # Converte as notas de strings para floats
    return sum(notas) / len(notas)

def gerar_arquivo_com_medias(arquivo_alunos, arquivo_notas, arquivo_medias):
    try:
        with open(arq_alunos, 'r') as alunos_file, open(arq_notas, 'r') as notas_file, open(arquivo_medias, 'w') as medias_file:
            for nome, notas_str in zip(alunos_file, notas_file):
                nome = nome.strip()
                notas = notas_str.split()
                media = calcular_media(notas)
                medias_file.write(f"{nome}: {media:.2f}\n")
        print(f"As médias foram calculadas e escritas em '{arquivo_medias}'.")
    except FileNotFoundError:
        print("Um dos arquivos não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    arq_alunos = input("Digite o nome do arquivo com os nomes dos alunos: ")
    arq_notas = input("Digite o nome do arquivo com as notas dos alunos: ")
    arquivo_medias = input("Digite o nome do arquivo de destino para as médias: ")

    gerar_arquivo_com_medias(arq_alunos, arq_notas, arquivo_medias)

