from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
import json
wb = load_workbook('tabelaCarros.xlsx')
wb = wb.active

# Pergunta quantidade de colunas 
qtdCol = int(input("Insira a quantidade de colunas da tabela: "))
qtdLinhas = int(input("Insira a quantidade de linhas da tabela: "))

dados = {}

for col in range(0,qtdCol):
    letra = 65 + col
    letra = chr(letra)
    celula = f"{letra}1"
    informacoesCelula = []
    for lin in range(2,qtdLinhas+1):    
        valorCol = f"{letra}{lin}"
        informacoesCelula.append(wb[valorCol].value)
    dados[wb[celula].value] = informacoesCelula

dadosTratados = []
def formataJson():
    for i in range(len(dados) + 1):
        idTemporario = dados['id'][i]
        carroTemporario = dados['carros'][i]
        potenciaTemporario = dados['potencia'][i]
        anoTemporario = dados['ano'][i]
        objTemporario = {
            "id":idTemporario,
            "carros":carroTemporario,
            "potencia":potenciaTemporario,
            "ano":anoTemporario
        }
        dadosTratados.append(objTemporario)
formataJson()
arquivo = open("InfosExcel.json",'w')
json.dump(dadosTratados,arquivo,indent=4)