def calcular_media(notas_str):
    notas = [float(nota) for nota in notas_str.split()]
    return sum(notas) / len(notas)

def gerar_arquivo_com_medias():
    arquivo_alunos = "alunos.txt" 
    arquivo_notas = "nota.txt"   
    arquivo_medias = "media.txt" 

    try:
        with open(arquivo_alunos, 'r') as alunos_file, open(arquivo_notas, 'r') as notas_file, open(arquivo_medias, 'w') as medias_file:
            for nome, notas_str in zip(alunos_file, notas_file):
                nome = nome.strip()
                media = calcular_media(notas_str)
                medias_file.write(f"{nome}: {media:.2f}\n")
        print(f"As médias foram calculadas e escritas em '{arquivo_medias}'.")
    except FileNotFoundError:
        print("Um dos arquivos não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    gerar_arquivo_com_medias()



