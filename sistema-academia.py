alunos = [{'nome': 'João Felix', 'cpf': '02323249103', 'altura': 1.70, 'peso': 75, 'imc': '', 'resultado': 'Indisponível'},
          {'nome': 'João Junior', 'cpf': '0232323403', 'altura': 1.60, 'peso': 70, 'imc': '', 'resultado': 'Indisponível'},

          ]

#------- Métodos do sistema ------------


def imprimir_alunos():
    for aluno in alunos:
        print(f"{aluno['nome']}---------"
              f"{aluno['cpf']}-----"
              f"{aluno['altura']}----"
              f"{aluno['peso']}----"
              f"{aluno['imc']}----"
              f"{aluno['resultado']}")


def inserir_alunos(nome_aluno, cpf, altura, peso, imc, resultado):
    alunos.append({
        'nome' : nome_aluno,
        'cpf' : cpf,
        'altura' : altura,
        'peso' : peso,
        'imc' : imc,
        'resultado' : resultado
    })


def buscar_aluno(cpf):
    for aluno in alunos:
        if aluno['cpf'] == cpf:
            print(f"{aluno['nome']}---------"
                  f"{aluno['cpf']}-----"
                  f"{aluno['altura']}----"
                  f"{aluno['peso']}----"
                  f"{aluno['imc']}----"
                  f"{aluno['resultado']}")
        else:
            print('Aluno não encontrado')
        break

def excluir_aluno(cpf):
    for aluno in alunos:
        if aluno['cpf'] == cpf:
            alunos.remove(aluno)
            print(f'Aluno {aluno["nome"]} removido com sucesso!')


def atualizar_imc():
    for aluno in alunos:
        imc = aluno['peso'] / (aluno['altura'] * aluno['altura'])
        aluno['imc'] = round(imc, 2)
        if imc < 16:
            aluno['resultado'] = 'Subpeso Severo'
        elif imc >= 16 and imc <= 19.9:
            aluno['resultado'] = 'Subpeso'
        elif imc >= 20. and imc <= 24.9:
            aluno['resultado'] = 'Peso normal'
        elif imc >= 25 and imc <= 29.9:
            aluno['resultado'] = 'Sobrepeso'
        elif imc >= 30 and imc <= 39.9:
            aluno['resultado'] = 'Obesidade grau 1'
        elif imc > 40:
            aluno['resultado'] = 'Obesidade Mórbida'


def aluno_maior_imc():
    maior_imc = 0
    for aluno in alunos:
        if aluno['imc'] > maior_imc:
            maior_imc = aluno['imc']
            nome_aluno = aluno['nome']
    print(f'Olá {nome_aluno}, Seu IMC é {maior_imc}. Isso significa que você está com {aluno["resultado"]} ')




def imprimir_menu():
    print(f'-----------------------------------------'
          f'\n1 - Mostrar todos os alunos'
          f'\n2 - Buscar Aluno'
          f'\n3 - Incluir Aluno'
          f'\n4 - Excluir Aluno'
          f'\n5 - Atualizar IMC'
          f'\n6 - Aluno com maior IMC'
          f'\n-----------------------------------------')


while True:
    imprimir_menu()
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        imprimir_alunos()
    elif opcao == 2:
        cpf = input('Digite o CPF do aluno: ')
        buscar_aluno(cpf)
    elif opcao == 3:
        nome_aluno = input('Digite o nome do aluno: ')
        cpf = input('Digite o CPF do aluno sem pontuação: ')
        altura = float(input('Digite a altura do aluno em Metros: '))
        peso = float(input('Digite o peso do aluno em Quilogramas(Kg): '))
        imc = peso / (altura * altura)
        inserir_alunos(nome_aluno, cpf, altura, peso, imc, '')
        atualizar_imc()
    elif opcao == 4:
        cpf = input('Digite o CPF do aluno: ')
        excluir_aluno(cpf)
    elif opcao == 5:
        atualizar_imc()
        print('IMC atualizado com sucesso!')
    elif opcao == 6:
        aluno_maior_imc()
    elif opcao == 0:
        break
    else:
        print('Opção inválida!')
