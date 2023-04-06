from clubes import Clube
from banca import Banca
from tratamentodeinformacoe import Informacoes



nomeusuario = Informacoes("arthur", "banana321")

nomeusuario.informações_de_usuario()
nomeusuario.tratamento_de_entrada()
if nomeusuario.tratamento_de_entrada() == False:
    print("ERROR")
elif nomeusuario.tratamento_de_entrada() == True:
    print("Acesso Concluido!")
else:
    print("Erro desconhecido 10 FAVOR CONTATAR SUPORTE")



'''
ORDEM DE CRIAÇÃO DO MAIN

Inicializar a classe Informacoes
    Inicializar a classe Banca
        Organizar todas as infors da Banca
            Inicializar bando de dados
                selecionar clube
                    se pesqusar clubes Inicializar classse Clubes
'''

'''
exentradas = ["2", "12", "9", "6"]
exsaidas = ["12", "10", "8",]

x = Banca(0, 0, 0, exentradas, exsaidas)

x.entradas()

listadevitorias = [5, 4, 3, 2, 1]
#nomedoclube = input("Insira o nome do clube ")
lsitadederrotas = [3, 2, 1]
listadesfalques = ["pedro", "gabirel"]
infoadversarios = ["contrataram o batman"]


!!!!!!! Nessa parte é um exemplo de uso da entrada e tratamento de usuario!!!!!!!!!


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
'''