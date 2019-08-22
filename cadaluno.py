arquivo = "alunos.db"

nomealuno=input("Digite o nome do aluno a ser cadastrado: ")

with open(arquivo, 'a') as bancodedados:
  bancodedados.write (nomealuno + '\n')
  bancodedados.close
