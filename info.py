

def informações_de_usuario ():
    
    nome = list(input("Insira Seu nome: "))
    senha = list(input("Insira sua senha: "))

    print (senha)
    print (nome)
    
    return nome




def tratamento_de_entrada(nome):

    listadeproibicao = "123456789"


    for numero in nome:
        if numero in listadeproibicao:
            print ("ERROR!!! NAO ADICIONAR NUMEROS")
            return informações_de_usuario()
        
        
        

