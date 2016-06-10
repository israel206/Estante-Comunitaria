def lerCodigo():
    while True:
        codigo = input("Digite o código do livro:")
        if len(codigo) == 4:
            return codigo
        else:
            print("Erro!!! - O código deve conter 4 caracteres.")
def lerTitulo():
    while True:
        titulo = input("Digite o título do livro:")
        if len(titulo) < 4 or len(titulo) > 30:
            print("Erro!!! - O título deve conter de 4 a 30 caracteres.")
        else:
            return titulo
def lerAutor():
    while True:
        autor = input("Digite o nome do autor(a):")
        if len(autor) < 8 or len(autor) > 30:
            print("Erro!!! - O nome do autor deve conter de 8 a 40 caracteres.")
        else:
            return autor

def lerOpcoes():
    opcoes = [1,2,3,4,5]
    while True:
        try:
            opcao = int(input("Informe a opção:"))
            if opcao not in opcoes:
                print("ERRO!!! - As opções são: 1,2,3,4 ou 5")
            else:
                return opcao
        except:
            print("ERRO!!! - As opções são: 1,2,3,4 ou 5 | Não pode conter letras!")
          
def listarLivros():
  while True:
      entrada = input("Deseja listar os livros?[S/N]:")
      if entrada == "S" or entrada == "s":
        return True
      elif entrada == "N" or entrada == "n":
        return False
      else:
          print("ERRO!!! - Entrada Inválida, Digite 'S'|'s' ou 'N'|'n'")

def cadastrarLivro():
  while True:
      entrada = input("Deseja cadastrar livro?[S/N]:")
      if entrada == "S" or entrada == "s":
        return True
      elif entrada == "N" or entrada == "n":
        return False
      else:
          print("ERRO!!! - Entrada Inválida, Digite 'S'|'s' ou 'N'|'n'")

