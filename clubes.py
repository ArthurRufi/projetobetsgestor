class Clube:
    
    listadevitorias = []
    
    def __init__(self, nome , emblema, vitorias, derrotas, adversarios):
    
        self._nome = nome
        self._emblema = emblema
        self._vitorias = vitorias
        self._derrotas = derrotas
        self._adverarios = adversarios


    def nmvitorias(self):
       
       vitorias = self._vitorias
       print (vitorias)
       

    def nmderrotas(self):

        derrotas = self._derrotas
        print (derrotas)


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
    