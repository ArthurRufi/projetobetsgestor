class Banca():
    def __init__(self, saldo, depositos, saques, entradas, saidas):
        self._saldo = saldo
        self._depositos = depositos
        self._saques = saques
        self._extrato_entradas = entradas
        self._saidas = saidas
    

    def entradas(self):
        
        extrato_entradas_int =  [int(x) for x in self._extrato_entradas] 
        soma_entradas = sum(extrato_entradas_int)
        
         
        while True:

            escolha = int(input("(1)Soma de Entradas\n(2)Entradas detalhadas\nESCOLHA: "))
            if escolha == 1:
                print(soma_entradas)
                return False
            elif escolha == 2:
                print (extrato_entradas_int)
                return False
            else:
                print("Escolha um numero valido!!!")
                return True


    def saidas(self):
        
        extratodesaidas = [int (x) for x in self._saidas]
        somasaidas = sum(extratodesaidas)
    
        while True:
    
            escolha = int(input("(1)Soma de saidas\n(2)Saidas detalhadas\nESCOLHA: "))


            if escolha == 1:
                print(somasaidas)
                return False
            elif escolha == 2:
                print (extratodesaidas)
                return False
            else:
                print("Escolha um numero valido!!!")
                continue


    def retornos_do_mes(self, listaderetornos):

       self._retornos = listaderetornos
       extratoderetornos = [float (r) for r in listaderetornos]
       '''
       Esse metodo deve ser chamado sempre na vidarada de cada mês para interagir com o banco de dados, pegando todos os retornos do mês e somando todos
       colocando esse resumo em mais uma tabela do banco de dados chamada de RETORNOSPORMES para resumir os retornos do mês
       '''
       somadosretornosdomes = sum(extratoderetornos)

       return somadosretornosdomes
    

    def perdas_do_mes(self, perdasdomes):

        self._perdas = perdasdomes
        extratodeperdas = [float (p) for p in perdasdomes]
        somadeperdasdomes = sum(extratodeperdas)
        '''
        Esse metodo faz exatamente a mesma coisa do metodo retornos_do_mes, sendo que esse metodo joga os joga as somas para uma tabela que deve ser nomeada
        de PERDADOSMESES.
        '''
        return somadeperdasdomes