##################################################################################################
'''AC_Detran'''
##################################################################################################
print("Iniciando..")

class Multa:
    
    def __init__(self, valor: float, motivo: str, data: str, placa: str):
        self._valor = valor #DoubleType
        self._motivo = motivo #StringType
        self._data = data #DateType
        self._placa = placa #StringType

    def getValor(self):
        return self._valor

    def getMotivo(self):
        return self._motivo
    
    def getData(self):
        return self._data

    def getplaca(self):
        return self._placa

class Ocorrencia:
    
    def __init__(self, placa: str, dataHora: str, nomeLogradouro: str, velocidadeMedia: int, tipoVeiculo: int):
        self._placa = placa #StringType
        self._dataHora = dataHora #DateType
        self._nomeLogradouro = nomeLogradouro #StringType
        self._velocidadeMedia = velocidadeMedia #IntType
        self._tipoVeiculo = tipoVeiculo #IntType
        
    def getplaca(self):
        return self._placa

    def getDataHora(self):
        return self._dataHora

    def getNomeLogradouro(self):
        return self._nomeLogradouro

    def getVelocidadeMedia(self):
        return self._velocidadeMedia

    def getTipoVeiculo(self):
        return self._tipoVeiculo

class BaseDeDados:

    def __init__(self, ocorrenciasSemProcessar, ocorrenciasProcessadas, multas, regras):
        self._ocorrenciasSemProcessar = [] #Type
        self._ocorrenciasProcessadas = [] #Type
        self._multas = [] #Type
        self._regras = [] #Type
    
    def getValor(self):
        return self._ocorrenciasSemProcessar

    def getMotivo(self):
        return self._ocorrenciasProcessadas
    
    def getData(self):
        return self._multas

    def getplaca(self):
        return self._regras
    
class RegraVelocidade:

    def __init__(self,velocidadeMaxima: int, nomeLogradouro: str, porcentagemMultaMedia: float, porcentagemMultaGrave: float):
        self._velocidadeMaxima = velocidadeMaxima #IntType
        self._nomeLogradouro = nomeLogradouro #StringType
        self._porcentagemMultaMedia = 0.1 #DoubleType = 0.1
        self._porcentagemMultaGrave = 0.4 #DoubleType = 0.4

    def getValor(self):
        return self._velocidadeMaxima

    def getMotivo(self):
        return self._nomeLogradouro
    
    def getData(self):
        return self._porcentagemMultaMedia

    def getplaca(self):
        return self._porcentagemMultaGrave

class RegraRodizio:

    def __init__(self, finalPlaca: int, logradourosAfetados: str, diaDaSemana: int, tipoVeiculo: int):
        self._finalPlaca = finalPlaca #IntType
        self._logradourosAfetados = [] #StringType
        self._diaDaSemana = diaDaSemana #IntType
        self._tipoVeiculo = tipoVeiculo #IntType

    def getValor(self):
        return self._finalPlaca

    def getMotivo(self):
        return self._logradourosAfetados
    
    def getData(self):
        return self._diaDaSemana

    def getplaca(self):
        return self._tipoVeiculo



class RegraMulta:

    def __init__(self, valorMultaMedia: float, valorMultaGrave: float, valorMultaLeve: float):
        self._valorMultaLeve = float(100,00)
        self._valorMultaMedia = float(150,00)
        self._valorMultaGrave = float(200,00)
        

    def getValor(self):
        return self._valorMultaMedia

    def getMotivo(self):
        return self._valorMultaGrave
    
    def getData(self):
        return self._valorMultaLeve

class RegraCorredorOnibus:

    def __init__(self, horaInicial: int, horaFinal: int, nomeLogradouro: str):
        self._horaInicial = horaInicial
        self._horaFinal = horaFinal
        self._nomeLogradouro = nomeLogradouro
    
    def getValor(self):
        return self._horaInicial

    def getMotivo(self):
        return self._horaFinal
    
    def getData(self):
        return self._nomeLogradouro



