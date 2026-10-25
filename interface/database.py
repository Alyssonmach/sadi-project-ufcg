import pandas as pd
import os

INTERFACE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data_csv(csv_file = 'carros_cadastro.csv'):
    '''
    Função para carregar os dados do CSV.

    Inputs:
        csv_file (str) -> caminho relativo onde está o arquivo CSV.
    
    Returns:
        dataframe (pd) -> base de dados carregada a partir de um CSV.
    '''

    csv_path = csv_file if os.path.isabs(csv_file) else os.path.join(INTERFACE_DIR, csv_file)
    if os.path.exists(csv_path): dataframe =  pd.read_csv(csv_path)
    else: dataframe = pd.DataFrame(columns=['Placa', 'Nome', 'CPF'])

    return dataframe

def save_data_csv(df, csv_file = 'carros_cadastro.csv'):
    '''
    Função para salvar os dados no CSV

    Inputs:
        df (pd) -> dataframe do pandas carregado.
        csv_file (str) -> caminho relativo do arquivo CSV a ser salvo.
    '''

    csv_path = csv_file if os.path.isabs(csv_file) else os.path.join(INTERFACE_DIR, csv_file)
    df.to_csv(csv_path, index=False)

def add_car(placa, nome, cpf):
    '''
    Função para cadastrar um novo carro.

    Inputs:
        placa (str) -> Informações da placa do usuário.
        nome (str) -> Informações do nome do usuário.
        cpf (str) -> Informações de CPF do usuário.
    '''

    df = load_data_csv()
    if placa in df['Placa'].values:
        print(f"Erro: O carro com a placa {placa} já está cadastrado.")
    else:
        novo_carro = pd.DataFrame({'Placa': [placa], 'Nome': [nome], 'CPF': [cpf]})
        df = pd.concat([df, novo_carro], ignore_index=True)
        save_data_csv(df)
        print(f"Carro com a placa {placa} cadastrado com sucesso.")

def remove_car(placa):
    '''
    Função para remover um carro da base de dados.

    Inputs:
        placa (str) -> Placa a ser removida da base de dados.
    '''
    df = load_data_csv()
    if placa not in df['Placa'].values:
        print(f"Erro: O carro com a placa {placa} não está cadastrado.")
    else:
        df = df[df['Placa'] != placa]
        save_data_csv(df)
        print(f"Carro com a placa {placa} removido com sucesso.")
