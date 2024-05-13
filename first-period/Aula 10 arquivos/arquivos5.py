def alterar_nota(arquivo_medias, nome_aluno, nova_nota):
    try:
        with open(arquivo_medias, 'r') as arquivo:
            linhas = arquivo.readlines()

        encontrado = False
        for i, linha in enumerate(linhas):
            if nome_aluno in linha:
                linhas[i] = linha.replace(linha.split(':')[1].strip(), f' {nova_nota}\n')
                encontrado = True
                break

        if not encontrado:
            print(f"Aluno '{nome_aluno}' não encontrado no arquivo de médias.")
            return

        with open(arquivo_medias, 'w') as arquivo:
            arquivo.writelines(linhas)

        print(f"A nota do aluno '{nome_aluno}' foi alterada com sucesso.")
    except FileNotFoundError:
        print("O arquivo de médias não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    arquivo_medias = "media.txt"  # Nome do arquivo com as médias dos alunos

    nome_aluno = input("Digite o nome do aluno para alterar a nota: ")
    nova_nota = input("Digite a nova nota: ")

    alterar_nota(arquivo_medias, nome_aluno, nova_nota)

