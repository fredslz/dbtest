arquivo = "alunos.db"

with open(arquivo, 'r') as myfile:
  conteudo_arquivo=list(myfile.readlines())

for linha in conteudo_arquivo:
  print (linha)
