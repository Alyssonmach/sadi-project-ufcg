import matplotlib.pyplot as plt
import streamlit as st 
import yaml
import os

# Configurando alguns parâmetros da página no navegador
st.set_page_config(page_title = 'SADI', layout = "wide")

def load_yaml(archive = 'config.yaml'):
    '''
    Função que carrega os dados em um dicionário a partir de um arquivo YAML.

    Inputs:
        archive (str) -> caminho local do arquivo YAML.
    
    Returns:
        yaml_dict (dict) -> dicionário com as variáveis do YAML.
    '''

    with open(archive, 'r') as file:
        yaml_dict = yaml.safe_load(file)
    
    return yaml_dict

# Parâmetros possíveis de serem atualizados na interface
STATUS_ANALYSIS = ['Em Espera', 'Aprovado', 'Reprovado']
PLATE_NUMBER = ['BCV6189', 'RI02A19', 'Em Espera']
STATUS_MOTOR = ['Fechado', 'Abrindo', 'Aberto', 'Fechando']
IMAGES = ['car1.jpeg', 'car2.jpg', 'not-car.jpg']

# Carregando os dados do arquivo YAML
data = load_yaml()
status_anaysis = data['status_analysis']
status_motor = data['status_motor']

# Atualizando os parâmetros atuais mostráveis na interface
if status_anaysis == STATUS_ANALYSIS[0]: plate_number, images = PLATE_NUMBER[2], IMAGES[2]
elif status_anaysis == STATUS_ANALYSIS[1]: plate_number, images = PLATE_NUMBER[0], IMAGES[0]
elif status_anaysis == STATUS_ANALYSIS[2]: plate_number, images = PLATE_NUMBER[1], IMAGES[1]
image = plt.imread(f'assets/{images}')

# Cabeçalho da Página
st.markdown('# Sistema de Estacionamento Inteligente')
st.divider()

# Personalizando a primeira parte do corpo da página (Informações de Inferências)
col1, col2, col3 = st.columns(spec = 3)

with col1: st.image(image = image, caption = 'Imagem Capturada', width = 400)

with col2:
    col1, col2 = st.columns(spec = [4,6])
    with col1: st.text('Status de Análise: ')
    with col2: st.warning(status_anaysis)
    st.divider()
    col1, col2 = st.columns(spec = [4,6])
    with col1: st.text('Número da Placa: ')
    with col2: st.warning(plate_number)
    st.divider()
    col1, col2 = st.columns(spec = [4,6])
    with col1: st.text('Status do Motor: ')
    with col2: st.error(status_motor)

with col3:
    st.text('Frames de Análise')
    col1, col2 = st.columns(2)
    with col1: st.image(image)
    with col2: st.image(image)

    col1, col2 = st.columns(2)
    with col1: st.image(image)
    with col2: st.image(image)

st.divider()

# Personalizando a segunda parte do corpo da página (Atualização na base de dados)

if 'tried_login' not in st.session_state: st.session_state.tried_login = False
if 'sucessfully_login' not in st.session_state: st.session_state.sucessfully_login = False

with st.expander('Acesso do Administrador'):
    # Parte que deve ser mostrada caso o usuário não esteja logado no sistema
    if st.session_state.sucessfully_login == False:
        col1, col2 = st.columns(2)
        with col1: login = st.text_input(label = 'Login: ')
        with col2: password = st.text_input(label = 'Senha:')
        state = st.button('Entrar no Sistema')

        if st.session_state.tried_login == True:
            st.error('Credenciais Inválidas, tente novamente!')

        if state:
            st.session_state.tried_login = True
            if login == 'admin' and password == '1234':
                st.session_state.sucessfully_login = True
    # Parte mostrada quando o usuário consegue logar com sucesso na área restrita
    else:
        logoff = st.button('Sair da Área Restrita')
        if logoff:
            st.session_state.tried_login = False
            st.session_state.sucessfully_login = False
