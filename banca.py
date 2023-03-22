class Banca():
    def __init__(self, saldo, depositos, saques):
        self._saldo = saldo
        self._depositos = depositos
        self._saques = saques
        
    

    def entradas(self, entradas):
       
        extratodeentradas = []
        self._entradas = entradas
        extratodeentradas.append(entradas)       


    def saidas(self, saidas):
        
        extratodesaidas = []
        self._saidas = saidas
        extratodesaidas.append(saidas)    
        pass


    def retornos_do_mes(self, listaderetornos):

        retornodomes = []
        self._retornos = listaderetornos
        retornodomes.append(listaderetornos)
        pass


    def perdas_do_mes(self, perdasdomes):

        perdadidosdomes = []
        self._perdasdomes = perdasdomes
        perdadidosdomes.append(perdasdomes)
        pass