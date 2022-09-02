def coletar_notas():
    QNTD_NOTAS = 3
    notas = []
    for i in range(QNTD_NOTAS):
        nota = float(input(f'Nota {i+1}: '))
        notas.append(nota)
    return notas

def preencher_turma(qtde_alunos):
    turma = []
    for i in range(qtde_alunos):
        print(f'{i+1}º aluno: ')
        notas_aluno = coletar_notas()
        turma.append(notas_aluno)
    return turma

def calcular_media(notas_aluno):
    soma = 0
    for nota in notas_aluno:
        soma += nota
    return soma / len(notas_aluno)

def resumo_turma(turma):
    for aluno in turma:
        media = calcular_media(aluno)
        print(f'Notas do aluno: {aluno}\nMédia: {media:.2f}')  

def main():
    qtde_alunos = int(input('Quantidade de alunos: '))
    turma = preencher_turma(qtde_alunos)
    resumo_turma(turma)

# Programa principal
main()