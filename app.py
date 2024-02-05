import os

restaurantes = [{'nome':'Praça', 'Categoria':'Japonesa','Ativo':False},
                {'nome':'Pizza Suprema', 'Categoria':'Pizza','Ativo':True},
                {'nome':'Cantina', 'Categoria':'Italiano','Ativo':False}]



def exibir_nome_do_programa():
    '''Essa função serve para exibir o título personalizado do programa'''
    print('''

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████───██████████████─████████████████──────██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░████████░░██──────██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██────██░░██──────██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
─██░░██████████─██░░██████░░██─██░░██████░░████─██░░██──██░░██─██░░████████░░██──────██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████░░██─██░░██████░░██─██░░████████░░██─██░░██──██░░██─██░░██████░░████──────██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
─────────██░░██─██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─██░░██──██░░██────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
─██████████░░██─██░░██──██░░██─██░░████████░░██─██░░██████░░██─██░░██──██░░██████────██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──██████─████████████████─██████████████─██████──██████████────██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
      ''')
    
def voltar_ao_menu_principal():
    '''Essa função pede uma confirmação e limpa a tela, voltando pro menu'''
    input('\ndigite uma tecla para voltar para o menu')
    main()

def exibir_subtitulo(texto):
    '''Essa função exibe o subtitulo com o parametro passado'''
    os.system('cls')
    print(texto)
    print('==============================')

def exibir_opcoes():
    '''Essa função exibe as opções no menu inicial'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair')

def finalizar_app():
    '''Essa função finaliza o app'''
    exibir_subtitulo('Finalizando App')

def opcao_invalida():
    ''' Essa função mostra quando a opção escolhida é inválida'''
    print('opção inválida\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função controla a tela de cadastro de novos restaurantes'''
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    nome_do_restaurante = input('Digite o nome do Restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante, 'Categoria': categoria, 'Ativo':False}

    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função '''
    os.system('cls')
    exibir_subtitulo('Listando Restaurantes Restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['Categoria']
        ativo = 'Ativado' if restaurante['Ativo'] else 'Desativado'
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')


    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando Estado')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('não encontrado')
    voltar_ao_menu_principal()
    

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            print('Saindo')
            finalizar_app()
            
        else:
            opcao_invalida()

    except: opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()