from clubes import Clube
from banca import Banca
from tratamentodeinformacoe import Informacoes








listadevitorias = [5, 4, 3, 2, 1]
#nomedoclube = input("Insira o nome do clube ")
lsitadederrotas = [3, 2, 1]
listadesfalques = ["pedro", "gabirel"]
infoadversarios = ["contrataram o batman"]


inputnome = input("Insira seu nome ")
inputsenha = input("Insira sua senha ")
nome = Informacoes(inputnome, inputsenha)
permission = nome.tratamento_de_entrada(inputnome)
if not permission:
    print("Por favor, insira um nome válido sem números proibidos.")
else:
    lista = nome.informações_de_usuario(inputnome, inputsenha)
    print("Informações de usuário:", lista)



#clube  = Clube(nomedoclube, "333")

#clube.nmvitorias(listadevitorias)

'''nome = informações_de_usuario()
tratamento_de_entrada(nome)
'''

'''
if __name__ == "__main__":
   
    saldo = (1500)
    depositos = ("lista de destino")
    saques = ("lista de saques")

    infbanca = Banca(saldo, depositos, saques)

    print (infbanca._saldo)
'''