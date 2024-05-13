conta = int(input("Digite o numero da conta:"))

while(conta != -1):
    saldo = float(input("Insira seu saldo na conta:"))
    if saldo >= 10000:
        taxa = saldo * 0.001
    else:
        taxa = saldo * 0.003

    nvsaldo = saldo - taxa
    print("O valor dos serviços = {0:.2f}".format(taxa))
    print("O saldo atual = {0:.2f}".format(nvsaldo))
    conta = int(input("Digite o numero da conta:"))
