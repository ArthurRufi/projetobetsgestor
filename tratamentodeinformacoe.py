class Informacoes:
    
    def __init__(self, nome1, senha):
        self.nomel = nome1
        self.senhal = senha


    def informações_de_usuario(self, nome, senha):
        nomelist = list(nome)
        senhalist = list(senha)
        return nomelist


    def tratamento_de_entrada(self, nomeparatratar):
        listadeproibicao = "123456789"
        permission = False
        for numero in nomeparatratar:
            if numero in listadeproibicao:
                print("ERROR!!! NAO ADICIONAR NUMEROS")
                permission = False
                break
            else:
                permission = True
        return permission

