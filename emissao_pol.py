
# =====================================================
## Verificacao das emissoes de gases medias poluentes diarias na rotatoria
# =====================================================
# imports

from matplotlib import pylab as plt
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openturns as ot
import openturns.viewer as viewer
import statsmodels.api as sm

# =====================================================
# Dados de entrada
input_file_path = "C:\\Users\\gusta\\Dropbox\\PC\\Documents\\mestrado\\etapa_de_programacao\\programacao_emissoes_gases\\dados_artigo.csv"
# =====================================================
# constantes 
v = 40 # KM/h
grad = 0 # gradiente da pista - inclinacao
alfa = 0.76 # aceleracao m/s2
## fatores de emissao por veic
car = 1.747 # kg de CO2/km
mot = 2.307
bus = 3.2 
cam = 3.2
comp_via = 151 # m
# =====================================================
separador = ';'

TME = []
vol_entrada = []
carros = []
motos = []
onibus = []
caminhao = []
with open(input_file_path, 'r', newline='') as csv_file:
    for line_number, content in enumerate(csv_file):
        if line_number:  # pula cabeçalho
            colunas = content.strip().split(separador)
            TME.append(float(colunas[0]))
            vol_entrada.append( float(colunas[1]) )
            carros.append( float(colunas[2]) )
            motos.append( float(colunas[3]) )
            onibus.append( float(colunas[4]) )
            caminhao.append( float(colunas[5]) )
# =====================================================            
tme_media = (np.mean([i for i in TME if isinstance(i, int) or isinstance(i, float)]))
#print(tme_soma)
vol_entrada_media = (np.mean([i for i in vol_entrada if isinstance(i, int) or isinstance(i, float)]))
emissao_car = car*(np.mean([i for i in carros if isinstance(i, int) or isinstance(i, float)]))
#print(emissao_car)
emissao_mot = mot*(np.mean([i for i in motos if isinstance(i, int) or isinstance(i, float)]))
#print(emissao_mot)
emissao_bus = bus*(np.mean([i for i in onibus if isinstance(i, int) or isinstance(i, float)]))
#print(emissao_bus)
emissao_cam = cam*(np.mean([i for i in caminhao if isinstance(i, int) or isinstance(i, float)]))
#print(emissao_cam)
#print(capacidade_soma)
#med_carros = 
taxa_veic_hora = 3600/vol_entrada_media
emissao_total = emissao_car + emissao_mot + emissao_bus + emissao_cam
#print(emissao_total)

# Vehicle Specific Power 
vsp = 1.1*v*alfa + 9.81*grad*0.132*v + 0.0003028*v**3
#print(vsp)
# estimativa da emissao
# Para o vsp calculado 52.82 e tabelado para os seguintes poluentes 
NO = 0.0179
HC = 0.0109
CO2 = 10.0884
CO = 0.8823 

# emissão total
E_NO = emissao_total*NO
#print(E_NO)
E_HC = emissao_total*HC
#print(E_HC)
E_CO2 = emissao_total*CO2
#print(E_CO2)
E_CO = emissao_total*CO
#print(E_CO)

# emissão para caminhao
E_NO = emissao_cam*NO
print(" o total de NO emitido é:", E_NO)
E_HC = emissao_cam*HC
print(" o total de HC emitido é:",E_HC)
E_CO2 = emissao_cam*CO2
print(" o total de CO2 emitido é:",E_CO2)
E_CO = emissao_cam*CO
print(" o total de CO emitido é:",E_CO)