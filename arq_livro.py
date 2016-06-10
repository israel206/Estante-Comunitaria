def armazenar(livro):
    arq = open("livros.txt", "a")
    arq.write("%s;%s;%s\n" % (livro[0],livro[1],livro[2]))
    arq.close()

def ler():
    livros = []
    arq = open("livros.txt", "r")
    linhas = arq.read().splitlines()
    for linha in linhas: 
        livros.append(linha.split(";"))
    return livros
    
def existeLivro(cod, livros):
    for livro in livros:
        if livro[0] == cod:
            return True
    return False

def apagarLivro(cod, livros):
    cont = 0
    for livro in livros:
        if livro[0] == cod:
            livros.pop(cont)
        cont += 1
    return livros

def atualizarLivros(livros):
    arq = open("livros.txt", "w")
    for livro in livros:
        arq.write("%s;%s;%s\n" % (livro[0],livro[1],livro[2]))
    arq.close()
