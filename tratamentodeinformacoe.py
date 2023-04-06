class Informacoes:
    
    def __init__(self, nome1, senha):
        self.nomel = nome1
        self.senhal = senha


    def informações_de_usuario(self):
        nomelist = list(self.nomel)
        self.letras = nomelist
        return self.letras


    def infomacoes_de_senha(self):
        senhalist = list(self.senhal)
        return print(senhalist)


    def tratamento_de_entrada(self):
        listadeproibicao = "123456789"
        permission = False
        for numero in self.letras:
            if numero in listadeproibicao:
                print("ERROR!!! NAO ADICIONAR NUMEROS")
                permission = False
                break
            else:
                permission = True
        
        return permission

