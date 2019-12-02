while True:
    print('Bem-vindo ao Validador de CPF!')
    cpf = input('Digite seu CPF: ')
    if cpf.isnumeric() and len(cpf) != 11 or not cpf.isnumeric():
        print('Por favor, digite apenas os 11 números.')
        continue
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    sequencia = cpf == novo_cpf[0] * 11
    if str(novo_cpf) == str(cpf) and not sequencia:
        print('CPF Válido')
    else:
        print('CPF Inválido')
    print("-"*10)

    def SAIR():
        while True:
            continua = str(input("""Deseja verificar outro CPF?
Digite 'S' para continuar.
Digite 'N' para sair. 
""").upper())
            if continua == 'S' or continua == 'N':
                break
            else:
                print('Opção inválida')
                continue
        if continua == 'S':            
            return '1'
        if continua == 'N':
            return '2'
    
    sair = SAIR()
    if sair == '1':
        print('-'*10)
        continue
    else:
        break
