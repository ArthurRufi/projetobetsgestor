class Clube:
    
    listadevitorias = []
    
    def __init__(self, nome, vitorias, derrotas, desfalques, adversarios):

        self._nome = nome
        self._vitorias = vitorias
        self._derrotas = derrotas
        self._desfalques = desfalques
        self._adversarios = adversarios


    def vitorias(self, vitorias, adversarios):
        
        self._vitorias = vitorias
        self._adversarios =  adversarios
        

        

    def derrotas(self, derrotas, adversarios):

        self._derrotas = derrotas
        self._adversarios = adversarios


    def avisos(self, avisos):
        
        self._avisos = avisos
        

    def desfalques(self, desfalques):
        
        self._desfalques = desfalques


    def alertas(self, alertas):
        
        self._alertas = alertas


    def estatisticas(self, estatisticas):
        
        self.dados = estatisticas