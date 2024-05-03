import time
import random

continuar_jogo = 's'

cor_do_navio = '\u001b[32m'
cor_da_agua = '\u001b[34m'
cor_de_acerto = '\u001b[31m'
reset = '\u001b[0m'

simbolo_do_navio = '▓'

navio_colorido = cor_do_navio + simbolo_do_navio + reset
navio_acertado = cor_de_acerto + simbolo_do_navio + reset
representacao_da_agua = cor_da_agua + simbolo_do_navio + reset

while continuar_jogo != 'n':

    def criar_mapa(tamanho):
        mapa = []
        for j in range(tamanho):
            linha = []
            for i in range(tamanho):
                linha.append(' ')
                if len(linha) == tamanho:
                    mapa.append(linha)
        return mapa

    def validar_posicao(mapa, tamanho_navio, linha, coluna, orientacao):
        is_valid = True
        if tamanho_navio > 0:
            if orientacao == 'v':
                for x in range(tamanho_navio):
                    if linha + x > len(mapa)-1 or mapa[linha+x][coluna] != ' ':
                        is_valid = False
            elif orientacao == 'h':
                for x in range(tamanho_navio):
                    if coluna + x > len(mapa[0])-1 or mapa[linha][coluna+x] != ' ':
                        is_valid = False
        return is_valid

    def posicionar_navios_automaticamente(mapa, tamanhos_navios):
        for tamanho_navio in tamanhos_navios:
            posicionado = False
            while not posicionado:
                linha_aleatoria = random.randint(0, len(mapa)-1)
                coluna_aleatoria = random.randint(0, len(mapa[0])-1)
                orientacao_aleatoria = random.choice(['h', 'v'])
                if validar_posicao(mapa, tamanho_navio, linha_aleatoria, coluna_aleatoria, orientacao_aleatoria):
                    if orientacao_aleatoria == 'v':
                        for incremento in range(tamanho_navio):
                            mapa[linha_aleatoria+incremento][coluna_aleatoria] = navio_colorido
                    elif orientacao_aleatoria == 'h':
                        for incremento in range(tamanho_navio):
                            mapa[linha_aleatoria][coluna_aleatoria+incremento] = navio_colorido
                    posicionado = True
        return mapa

    def posicionar_navios_jogador(mapa, tamanhos_navios, linha_inicial, coluna_inicial, orientacao):
        mapa_temporario = [linha[:] for linha in mapa]
        for tamanho_navio in tamanhos_navios:
            posicionado = False
            while not posicionado:
                if validar_posicao(mapa, tamanho_navio, linha_inicial, coluna_inicial, orientacao):
                    if orientacao == 'v':
                        for incremento in range(tamanho_navio):
                            mapa_temporario[linha_inicial+incremento][coluna_inicial] = navio_colorido
                    elif orientacao == 'h':
                        for incremento in range(tamanho_navio):
                            mapa_temporario[linha_inicial][coluna_inicial+incremento] = navio_colorido
                    posicionado = True
        return mapa_temporario

    def checar_derrota(mapa):
        for linha in mapa:
            if navio_colorido in linha:
                return False
        return True

    def mostrar_mapas(mapa_ia, mapa_jogador, nome_ia, nome_jogador):
        print(f'     COMPUTADOR - {nome_ia}                 JOGADOR - {nome_jogador}     \n')
        print('   A  B  C  D  E  F  G  H  I  J        A  B  C  D  E  F  G  H  I  J')
        for numero_linha in range(10):
            print(f'{numero_linha+1:2d}', end='')
            for coluna in range(10):
                print(f' {mapa_ia[numero_linha][coluna]} ', end='')
            print(f'  {numero_linha+1:2d}', end='')
            for coluna in range(10):
                print(f' {mapa_jogador[numero_linha][coluna]} ', end='')
            print(' ')
        print('   A  B  C  D  E  F  G  H  I  J        A  B  C  D  E  F  G  H  I  J')

    configuracao_navios = {
        'destroyer': 3,
        'porta_avioes': 5,
        'submarino': 2,
        'torpedeiro': 3,
        'cruzador': 2,
        'couracado': 4
    }

    paises_frotas = {
        'Brasil': {
            'cruzador': 1,
            'torpedeiro': 2,
            'destroyer': 1,
            'couracado': 1,
            'porta_avioes': 1
        }, 
        'Franca': {
            'cruzador': 3, 
            'porta_avioes': 1, 
            'destroyer': 1, 
            'submarino': 1, 
            'couracado': 1
        },
        'Australia': {
            'couracado': 1,
            'cruzador': 3, 
            'submarino': 1,
            'porta_avioes': 1, 
            'torpedeiro': 1
        },
        'Russia': {
            'cruzador': 1,
            'porta_avioes': 1,
            'couracado': 2,
            'destroyer': 1,
            'submarino': 1
        },
        'Japao': {
            'torpedeiro': 2,
            'cruzador': 1,
            'destroyer': 2,
            'couracado': 1,
            'submarino': 1
        }
    }

    alfabeto_para_colunas = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}

    cores_terminal = {
        'reset': '\u001b[0m',
        'red': '\u001b[31m',
        'black': '\u001b[30m',
        'green': '\u001b[32m',
        'yellow': '\u001b[33m',
        'blue': '\u001b[34m',
        'magenta': '\u001b[35m',
        'cyan': '\u001b[36m',
        'white': '\u001b[37m'
    }

    lista_paises = ['', 'Brasil', 'Franca', 'Australia', 'Russia', 'Japao']
    pais_computador = random.choice(['Brasil', 'Franca', 'Australia', 'Russia', 'Japao'])
    linha_divisoria = ' '
    linha_divisoria += '=' * 37
    linha_divisoria += ' '

    print(linha_divisoria)
    print('|', ' ' * (len(linha_divisoria) - 4), '|')
    print('| Bem-vindo ao INSPER - Batalha Naval |')
    print('|', ' ' * (len(linha_divisoria) - 4), '|')
    print(' =======   xxxxxxxxxxxxxxxxx   ======= \n')
    print('Iniciando o Jogo!\n')
    print(f'Computador está alocando os navios de guerra do país {pais_computador}...')
    print('Computador já está em posição de batalha!\n')

    print('1: Brasil\n  1 cruzador\n  2 torpedeiro\n  1 destroyer\n  1 couracado\n  1 porta-avioes\n')
    print('2: França\n  3 cruzador\n  1 porta-avioes\n  1 destroyer\n  1 submarino\n  1 couracado\n')
    print('3: Austrália\n  1 couracado\n  3 cruzador\n  1 submarino\n  1 porta-avioes\n  1 torpedeiro\n')
    print('4: Rússia\n  1 cruzador\n  1 porta-avioes\n  2 couracado\n  1 destroyer\n  1 submarino\n')
    print('5: Japão\n  2 torpedeiro\n  1 cruzador\n  2 destroyer\n  1 couracado\n  1 submarino\n')

    pais_escolhido = input('Qual o número da nação da sua frota? ')
    while True:
        if pais_escolhido not in ['1','2','3','4','5'] or lista_paises[int(pais_escolhido)] == pais_computador:
            print('\nOpção inválida')
            print('Você escolheu o mesmo país que o computador!')
            print('Por favor escolha outro país\n')
            pais_escolhido = input('Qual o número da nação da sua frota? ')
        if pais_escolhido in ['1','2','3','4','5']:
            break
    
    pais_escolhido = int(pais_escolhido)
    nome_pais_jogador = lista_paises[pais_escolhido]
    print(f'\nVocê escolheu a nação {nome_pais_jogador}! \n')

    mapa_principal = criar_mapa(10)
    mapa_jogador = criar_mapa(10)
    mapa_ia = criar_mapa(10)

    mostrar_mapas(mapa_principal, mapa_principal, pais_computador, nome_pais_jogador)
    print('\n')

    blocos_navios_jogador = []
    for tipo_navio, quantidade in paises_frotas[nome_pais_jogador].items():
        for _ in range(quantidade):
            print(f'Alocar: {tipo_navio} ({configuracao_navios[tipo_navio]} blocos)')
            while True:
                coluna_input = input('Coluna (A-J): ').upper()
                if coluna_input in alfabeto_para_colunas.keys():
                    coluna_escolhida = alfabeto_para_colunas[coluna_input]
                    break
                else:
                    print("Coluna inválida")

            while True:
                linha_input = input('Linha (1-10): ')
                if linha_input.isdigit() and 1 <= int(linha_input) <= 10:
                    linha_escolhida = int(linha_input) - 1
                    break
                else:
                    print("Linha inválida")

            while True:
                orientacao_input = input('Orientação (v para vertical, h para horizontal): ')
                if orientacao_input in ['v', 'h']:
                    orientacao_escolhida = orientacao_input
                    break
                else:
                    print("Orientação inválida")

            if validar_posicao(mapa_jogador, configuracao_navios[tipo_navio], linha_escolhida, coluna_escolhida, orientacao_escolhida):
                blocos_navios_jogador.append(configuracao_navios[tipo_navio])
                mapa_jogador = posicionar_navios_jogador(mapa_jogador, blocos_navios_jogador, linha_escolhida, coluna_escolhida, orientacao_escolhida)
                mostrar_mapas(mapa_principal, mapa_jogador, pais_computador, nome_pais_jogador)
                print('\n')
                break
            else:
                print("Posição inválida, tente novamente.")

    print('Todos os navios foram alocados!\n')

    blocos_navios_ia = []
    for tipo_navio, quantidade in paises_frotas[pais_computador].items():
        blocos_navios_ia.extend([configuracao_navios[tipo_navio]] * quantidade)
    
    mapa_ia = posicionar_navios_automaticamente(mapa_ia, blocos_navios_ia)
    
    print('Iniciando batalha naval!')
    for contagem in range(5, 0, -1):
        print(f'{contagem}')
        time.sleep(1)

    mostrar_mapas(mapa_principal, mapa_jogador, pais_computador, nome_pais_jogador)
    print('\n')

    while True:
        coluna_disparo = input("Coluna do disparo (A-J): ").upper()
        if coluna_disparo in alfabeto_para_colunas:
            coluna_disparo_index = alfabeto_para_colunas[coluna_disparo]
        else:
            print("Coluna inválida!")
            continue

        linha_disparo = input("Linha do disparo (1-10): ")
        if linha_disparo.isdigit() and 1 <= int(linha_disparo) <= 10:
            linha_disparo_index = int(linha_disparo) - 1
        else:
            print("Linha inválida!")
            continue

        if mapa_ia[linha_disparo_index][coluna_disparo_index] == " ":
            mapa_ia[linha_disparo_index][coluna_disparo_index] = representacao_da_agua
            mapa_principal[linha_disparo_index][coluna_disparo_index] = representacao_da_agua
            print(f'\nJogador --->>>> {coluna_disparo}{linha_disparo} Água!\n')
            jogada_continua = False
        elif mapa_ia[linha_disparo_index][coluna_disparo_index] == navio_colorido:
            mapa_ia[linha_disparo_index][coluna_disparo_index] = navio_acertado
            mapa_principal[linha_disparo_index][coluna_disparo_index] = navio_acertado
            print(f'\nJogador --->>>> {coluna_disparo}{linha_disparo} ACERTOU!\n')
            jogada_continua = False
        else:
            print('Você já atirou nesta posição, atire novamente!')
            jogada_continua = True

        if not jogada_continua:
            linha_ia = random.randint(0, 9)
            coluna_ia = random.choice(list(alfabeto_para_colunas.values()))

            while mapa_jogador[linha_ia][coluna_ia] == navio_acertado or mapa_jogador[linha_ia][coluna_ia] == representacao_da_agua:
                linha_ia = random.randint(0, 9)
                coluna_ia = random.choice(list(alfabeto_para_colunas.values()))

            if mapa_jogador[linha_ia][coluna_ia] == " ":
                mapa_jogador[linha_ia][coluna_ia] = representacao_da_agua
                print(f'Computador --->>>> Água na posição {coluna_ia}{linha_ia+1}!\n')
                mostrar_mapas(mapa_principal, mapa_jogador, pais_computador, nome_pais_jogador)
                print('\n')
            elif mapa_jogador[linha_ia][coluna_ia] == navio_colorido:
                mapa_jogador[linha_ia][coluna_ia] = navio_acertado
                print(f'Computador --->>>> ACERTOU na posição {coluna_ia}{linha_ia+1}!\n')
                mostrar_mapas(mapa_principal, mapa_jogador, pais_computador, nome_pais_jogador)
                print('\n')

        if checar_derrota(mapa_jogador):
            print('O jogo acabou! Você perdeu!')
            break
        elif checar_derrota(mapa_ia):
            print('O jogo acabou! Você ganhou!')
            break

    continuar_jogo = input('\nDeseja jogar novamente? (s/n) ').lower()
    if continuar_jogo == 'n':
        print('\nAté a próxima!\n')
        break

    while True:
        coluna_disparo = input("Coluna do disparo (A-J): ").upper()
        if coluna_disparo in alfabeto_para_colunas:
            coluna_disparo_index = alfabeto_para_colunas[coluna_disparo]
        else:
            print("Coluna inválida!")
            continue

        linha_disparo = input("Linha do disparo (1-10): ")
        if linha_disparo.isdigit() and 1 <= int(linha_disparo) <= 10:
            linha_disparo_index = int(linha_disparo) - 1
        else:
            print("Linha inválida!")
            continue

        if mapa_ia[linha_disparo_index][coluna_disparo_index] == " ":
            mapa_ia[linha_disparo_index][coluna_disparo_index] = representacao_da_agua
            mapa_principal[linha_disparo_index][coluna_disparo_index] = representacao_da_agua
            print(f'\nJogador --->>>> {coluna_disparo}{linha_disparo} Água!\n')
            jogada_continua = False
        elif mapa_ia[linha_disparo_index][coluna_disparo_index] == navio_colorido:
            mapa_ia[linha_disparo_index][coluna_disparo_index] = navio_acertado
            mapa_principal[linha_disparo_index][coluna_disparo_index] = navio_acertado
            print(f'\nJogador --->>>> {coluna_disparo}{linha_disparo} ACERTOU!\n')
            jogada_continua = False
        else:
            print('Você já atirou nesta posição, atire novamente!')
            continue

        if not jogada_continua:
            linha_ia, coluna_ia = random.randint(0, 9), random.choice(list(alfabeto_para_colunas.values()))
            while mapa_jogador[linha_ia][coluna_ia] in [navio_acertado, representacao_da_agua]:
                linha_ia, coluna_ia = random.randint(0, 9), random.choice(list(alfabeto_para_colunas.values()))

            if mapa_jogador[linha_ia][coluna_ia] == " ":
                mapa_jogador[linha_ia][coluna_ia] = representacao_da_agua
                print(f'Computador --->>>> Água na posição {chr(65 + coluna_ia)}{linha_ia+1}!\n')
            elif mapa_jogador[linha_ia][coluna_ia] == navio_colorido:
                mapa_jogador[linha_ia][coluna_ia] = navio_acertado
                print(f'Computador --->>>> ACERTOU na posição {chr(65 + coluna_ia)}{linha_ia+1}!\n')

            mostrar_mapas(mapa_principal, mapa_jogador, pais_computador, nome_pais_jogador)
            print('\n')
            if checar_derrota(mapa_jogador):
                print('O jogo acabou! Você perdeu!')
                break
            elif checar_derrota(mapa_ia):
                print('O jogo acabou! Você ganhou!')
                break
        resposta = input('\nDeseja jogar novamente? (s/n) ')
        if resposta.lower() == 'n':
            print('\nAté a próxima!\n')
            break
        elif resposta.lower() == 's':
            mapa_principal = criar_mapa(10)
            mapa_jogador = criar_mapa(10)
            mapa_ia = criar_mapa(10)
            mostrar_mapas(mapa_principal, mapa_jogador, pais_computador, nome_pais_jogador)
            continue
        else:
            print("Por favor, digite 's' para sim ou 'n' para não.")
            continue
    while True:
        print("\nÉ a sua vez de atirar!")
        coluna_disparo = input("Coluna do disparo (A-J): ").upper()
        if coluna_disparo in alfabeto_para_colunas:
            coluna_disparo_index = alfabeto_para_colunas[coluna_disparo]
        else:
            print("Coluna inválida!")
            continue

        linha_disparo = input("Linha do disparo (1-10): ")
        if linha_disparo.isdigit() and 1 <= int(linha_disparo) <= 10:
            linha_disparo_index = int(linha_disparo) - 1
        else:
            print("Linha inválida!")
            continue

        if mapa_ia[linha_disparo_index][coluna_disparo_index] == " ":
            mapa_ia[linha_disparo_index][coluna_disparo_index] = representacao_da_agua
            mapa_principal[linha_disparo_index][coluna_disparo_index] = representacao_da_agua
            print(f'\nJogador --->>>> {coluna_disparo}{linha_disparo} Água!\n')
        elif mapa_ia[linha_disparo_index][coluna_disparo_index] == navio_colorido:
            mapa_ia[linha_disparo_index][coluna_disparo_index] = navio_acertado
            mapa_principal[linha_disparo_index][coluna_disparo_index] = navio_acertado
            print(f'\nJogador --->>>> {coluna_disparo}{linha_disparo} ACERTOU!\n')
        else:
            print('Você já atirou nesta posição, atire novamente!')
            continue

        if checar_derrota(mapa_ia):
            print('O jogo acabou! Você ganhou!')
            break

        print("\nAgora é a vez do computador!")
        linha_ia, coluna_ia = random.randint(0, 9), random.choice(list(alfabeto_para_colunas.values()))
        while mapa_jogador[linha_ia][coluna_ia] in [navio_acertado, representacao_da_agua]:
            linha_ia, coluna_ia = random.randint(0, 9), random.choice(list(alfabeto_para_colunas.values()))

        if mapa_jogador[linha_ia][coluna_ia] == " ":
            mapa_jogador[linha_ia][coluna_ia] = representacao_da_agua
            print(f'Computador --->>>> Água na posição {chr(65 + coluna_ia)}{linha_ia+1}!\n')
        elif mapa_jogador[linha_ia][coluna_ia] == navio_colorido:
            mapa_jogador[linha_ia][coluna_ia] = navio_acertado
            print(f'Computador --->>>> ACERTOU na posição {chr(65 + coluna_ia)}{linha_ia+1}!\n')

        if checar_derrota(mapa_jogador):
            print('O jogo acabou! Você perdeu!')
            break

        mostrar_mapas(mapa_principal, mapa_jogador, pais_computador, nome_pais_jogador)
        print('\n')

        resposta = input('\nDeseja jogar novamente? (s/n) ')
        if resposta.lower() == 'n':
            print('\nAté a próxima!\n')
            break
        elif resposta.lower() == 's':
            mapa_principal = criar_mapa(10)
            mapa_jogador = criar_mapa(10)
            mapa_ia = criar_mapa(10)
            mostrar_mapas(mapa_principal, mapa_jogador, pais_computador, nome_pais_jogador)
            continue
        else:
            print("Por favor, digite 's' para sim ou 'n' para não.")
            continue

    print("Jogo finalizado. Obrigado por jogar Batalha Naval!")