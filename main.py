import pandas as pd
from datetime import datetime as dt

# path of metabase data archives
cliente_atendimento = pd.read_csv(r'C:\Users\welder.souza\Documents\Workspace\python_archives\secretaria\cliente-atendimento\meta.csv')
contato_secretaria_lite = pd.read_csv(r'C:\Users\welder.souza\Documents\Workspace\python_archives\secretaria\contato-secretaria-lite\meta.csv')
# visita_detalhada = pd.read_csv(r'C:\Users\welder.souza\Documents\Workspace\python_archives\secretaria\visita-detalhada\meta.csv')
cliente_lembrete = pd.read_csv(r'C:\Users\welder.souza\Documents\Workspace\python_archives\secretaria\cliente-lembrete\meta.csv')

# path for save final archives
path_atendimento = r'C:\Users\welder.souza\Documents\Workspace\daily_queries\cliente_atendimento'
path_secretaria_lite = r'C:\Users\welder.souza\Documents\Workspace\daily_queries\contato_secretaria_lite'
path_detalhada = r'C:\Users\welder.souza\Documents\Workspace\daily_queries\visita_detalhada'
path_cliente_lembrete = r'C:\Users\welder.souza\Documents\Workspace\daily_queries\cliente_lembrete'

# aux variable for quicksight data
aux_quick1 = pd.read_csv(r'C:\Users\welder.souza\Documents\Workspace\python_archives\secretaria\quick.csv')
aux_quick2 = pd.read_csv(r'C:\Users\welder.souza\Documents\Workspace\python_archives\secretaria\quick_data_with_obs.csv')

# variable for date time now
date_time = dt.today().strftime('%d-%m-%Y')

# merge cliente_atendimento with quick data
merge_client = pd.merge(cliente_atendimento, aux_quick1, on='codigo_cliente')
merge_client.set_index('codigo_cliente', inplace=True)

# merge contato_secretaria_lite with quick data
merge_lite = pd.merge(contato_secretaria_lite, aux_quick1, on='codigo_cliente')
merge_lite.set_index('codigo_cliente', inplace=True)

# merge visita_detalhada with quick data
# merge_visita = pd.merge(visita_detalhada, aux_quick1, on='codigo_cliente')
# merge_visita.set_index('codigo_cliente', inplace=True)

# merge cliente_lembrete with quick data
merge_lembrete = pd.merge(cliente_lembrete, aux_quick1, on='codigo_cliente')
merge_lembrete.set_index('codigo_cliente', inplace=True)

# Transform archives to CSV sep='\t'
merge_client.to_csv(path_atendimento+'\cliente_atendimento_(' + date_time + ').csv', sep ='\t')
merge_lite.to_csv(path_secretaria_lite+'\contato_secretaria_lite_(' + date_time + ').csv', sep ='\t')
# # merge_visita.to_csv('cliente_lembrete_(' + date_time + ').csv', sep ='\t')
merge_lembrete.to_csv(path_cliente_lembrete+'\cliente_lembrete_(' + date_time + ').csv', sep ='\t')



