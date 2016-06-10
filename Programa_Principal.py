import arq_livro as arq
import arq_tratamentoErro as arqTrat

def menu():
    print("╔═════════════════════╗")
    print("║■■■■■■■■■■■■■■■■■■■■■║")
    print("║ ESTANTE COMUNITÁRIA ║")
    print("║■■■■■■■■■■■■■■■■■■■■■║")
    print("║",6*" ","MENU",6*" ","","║")
    print("╠",2*" ","[1]Cadastrar",3*" ","╣")
    print("╠",2*" ","[2]Listar",3*" "," "*2,"╣")
    print("╠",2*" ","[3]Procurar",3*" "," ""╣")
    print("╠",2*" ","[4]Emprestar",3*" ","╣")
    print("╠",2*" ","[5]Sair",8*" ","╣")
    print("╚═════════════════════╝")

def cadastro():
    print("╔══════════════╗")
    print("║■■■■■■■■■■■■■■║")
    print("║   CADASTRO   ║")
    print("║■■■■■■■■■■■■■■║")
    print("╚══════════════╝")
    livro = []
    cod = arqTrat.lerCodigo()
    titulo = arqTrat.lerTitulo()
    autor = arqTrat.lerAutor()
    livro = cod,titulo,autor
    return livro

def listar(livros):
    print("╔════════════════════════════════════════════════════════════════════════════╗")
    print("║■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■║")
    print("║                                  LISTAR                                    ║")
    print("║■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■║")
    print("║  Código"," |"," "*10,"Título"," "*10,"|"," "*11,"Autor(a)"," "*11,"║")
    for livro in livros:
        linhaCod = " "*int(3-(len(livro[0]))/2)
        linhaTit =" "*int(13-(len(livro[1]))/2)
        linhaAut =" "*int(15-(len(livro[2]))/2)
        if len(livro[1])and len(livro[2])%2==0:
            print("║",linhaCod,livro[0],linhaCod,"|",linhaTit,livro[1],linhaTit,"|",linhaAut,livro[2],linhaAut,"║")
        elif len(livro[1])%2!=0 and len(livro[2])%2!=0:
            linhaTit = " "*((int(12-(len(livro[1]))/2)))
            print("║",linhaCod,livro[0],linhaCod,"| ",linhaTit,livro[1],linhaTit,"  |",linhaAut,livro[2],linhaAut," ║")
        elif len(livro[1])%2!=0 and len(livro[2])%2==0:
            print("║",linhaCod,livro[0],linhaCod,"| ",linhaTit,livro[1],linhaTit,"  | ",linhaAut,livro[2],linhaAut," ║")
        else:
            print("║",linhaCod,livro[0],linhaCod,"|",linhaTit,livro[1],linhaTit,"|",linhaAut,livro[2],linhaAut," ║")
    print("╚════════════════════════════════════════════════════════════════════════════╝")

def pesquisar(livros):
    print("╔══════════════╗")
    print("║■■■■■■■■■■■■■■║")
    print("║   PROCURAR   ║")
    print("║■■■■■■■■■■■■■■║")
    print("╚══════════════╝")
    cod = arqTrat.lerCodigo()
    if arq.existeLivro(cod,livros):
        print("O livro está na estante.")
    else:
        print("O livro não está na estante.")

def emprestimo(livros):
    print("╔══════════════╗")
    print("║■■■■■■■■■■■■■■║")
    print("║  EMPRÉSTIMO  ║")
    print("║■■■■■■■■■■■■■■║")
    print("╚══════════════╝")
    quant = False
    for livro in livros:
        quant = True       
    if quant == True:
        listarLivros = arqTrat.listarLivros()
        if listarLivros == True:
            listar(livros)
        cod = arqTrat.lerCodigo()   
        arq.atualizarLivros(arq.apagarLivro(cod,livros))
    elif quant == False:
        print("Não há livros na estante.")

livros = []
livro = []
livros = arq.ler()
opcao = ""
while opcao != 5:
    menu()
    opcao = arqTrat.lerOpcoes()
    if opcao == 1:
        livro = cadastro()
        arq.armazenar(livro)
        livros = arq.ler()
    elif opcao == 2:
        listar(livros)
    elif opcao == 3:
        pesquisar(livros)
    elif opcao == 4:
        emprestimo(livros)
        

        
