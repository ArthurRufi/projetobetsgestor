class Clube:
    
    listadevitorias = []
    
    def __init__(self, nome , emblema):

        self._nome = nome
        self._emblema = emblema


    def nmvitorias(self, vitorias, adversarios):
        self._vitorias = vitorias
        self._lutinhas = adversarios

        nv = 0
        for v in vitorias:
            nv += 1 
        
        print (nv)
        


    def nmderrotas(self, derrotas, adversarios):

        self._derrotas = derrotas
        self._adversarios = adversarios
        
        print(derrotas)


    def nmavisos(self, avisos):
        
        self._avisos = avisos
        print (avisos)


    def nmdesfalques(self, desfalques):
        
        self._desfalques = desfalques
        print (desfalques)


    def nmalertas(self, alertas):
        
        self._alertas = alertas
        print (alertas)


    def estatisticas(self, estatisticas):

        
        self._dados = estatisticas
        print(estatisticas)
    