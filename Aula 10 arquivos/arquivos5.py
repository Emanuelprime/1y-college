def alterar_nota(arq_alunos, aluno, nota_antiga, nova_nota):
    try:
        #abrir o arquivo para leitura
        with open(arq_alunos, 'r') as arquivo:
            linhas = arquivo.readlines()

        #procurar o aluno pelo nome
        encontrado = False
        for i, linha in enumerate(linhas):
            if linha.strip() == aluno:
                #encontrou o aluno, agora substituir a nota antiga pela nova
                linhas[i + 1] = nova_nota + '\n'
                encontrado = True
                break

        if not encontrado:
            print(f"Aluno '{aluno}' não encontrado no arquivo.")
            return

        #reabre o arquivo para escrita e reescrever as linhas atualizadas
        with open(arq_alunos, 'w') as arquivo:
            arquivo.writelines(linhas)

        print(f"A nota do aluno '{aluno}' foi alterada com sucesso.")
    except FileNotFoundError:
        print("O arquivo de alunos não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    arq_alunos = "alunos.txt"  #nome do arquivo com os nomes dos alunos

    aluno = input("Digite o nome do aluno para alterar a nota: ")
    nota_antiga = input("Digite a nota antiga: ")
    nova_nota = input("Digite a nova nota: ")

    alterar_nota(arq_alunos, aluno, nota_antiga, nova_nota)
