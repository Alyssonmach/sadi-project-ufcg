import streamlit as st 
import matplotlib.pyplot as plt

st.set_page_config(page_title = 'SADI', layout = "wide")

st.markdown('# Sistema de Estacionamento Inteligente')
st.divider()

col1, col2, col3 = st.columns(spec = 3)

with col1:
    image = plt.imread('assets/carro.jpeg')
    st.image(image = image, caption = 'Imagem Capturada', width = 400)

with col2:
    col1, col2 = st.columns(spec = [4,6])
    with col1: st.text('Status de Análise: ')
    with col2: st.warning('Analisando Placa...')
    st.divider()
    col1, col2 = st.columns(spec = [4,6])
    with col1: st.text('Número da Placa: ')
    with col2: st.warning('BCV6189')
    st.divider()
    col1, col2 = st.columns(spec = [4,6])
    with col1: st.text('Status do Motor: ')
    with col2: st.error('Fechado')

with col3:
    st.text('Frames de Análise')
    col1, col2 = st.columns(2)
    with col1: st.image(image)
    with col2: st.image(image)

    col1, col2 = st.columns(2)
    with col1: st.image(image)
    with col2: st.image(image)

st.divider()

if 'tried_login' not in st.session_state:
    st.session_state.tried_login = False

if 'sucessfully_login' not in st.session_state:
    st.session_state.sucessfully_login = False

with st.expander('Acesso do Administrador'):
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
    else:
        logoff = st.button('Sair da Área Restrita')
        if logoff:
            st.session_state.tried_login = False
            st.session_state.sucessfully_login = False
