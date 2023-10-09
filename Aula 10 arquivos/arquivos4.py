def exercicio4(arquivoNomes, arquivoNotas):
    nomes = open(arquivoNomes, 'r', encoding="utf-8")
    notas = open(arquivoNotas, 'r', encoding="utf-8")
    arquivoNomesNotas = open("4-listaMediasAlunos.txt", 'w+', encoding="utf-8")

    linhaNotas = notas.readline()
    linhaNomes = nomes.readline()

    while linhaNotas != "":
        listaNotas = linhaNotas.split(" ")
        nome = linhaNomes.replace("\n", "")
        soma = 0.0
        
        for item in listaNotas:
            indice = listaNotas.index(item)
            if "\n" in item:
                listaNotas[indice] = listaNotas[indice].replace("\n", "")
            soma += float(listaNotas[indice])
                
        media = "{:.2f}".format(soma / 3)
        alunoMedia = f'{nome:<20} {media}\n'
        arquivoNomesNotas.write(alunoMedia)
        linhaNotas = notas.readline()
        linhaNomes = nomes.readline()
        
    arquivoNomesNotas.close()
    nomes.close()
    notas.close()
    
exercicio4("4-listaNomesAlunos.txt", "4-listaNotasAlunos.txt")