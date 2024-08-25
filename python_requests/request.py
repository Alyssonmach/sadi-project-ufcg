import requests

def send_command(is_approved, server_connection = 'http://127.0.0.1:1880', nodered_post = '/comando'):
    '''
    Gera a comunicação entre o servidor Python e o servidor Node Red.

    Inputs:
        is_approved (bool) -> Indica se a entrada do carro foi aprovada ou reprovada.
        server_connection (str) -> URL de conexação do servidor Node Red ativo.
        nodered_post (str) -> diretório de acesso público para uploado de informações na conexão feita com o servidor.
    '''

    # URL de conexão com o servidor do Node Red
    url = server_connection + nodered_post 
    # Informações para comunicação com o servidor
    info = ["Acesso Permitido", "Acesso Negado", "Erro Interno"]

    # Define o tipo de mensagem a ser comunicada com o servidor
    if is_approved == True: data = info[0]
    elif is_approved == False: data = info[1]
    else: data = info[2]
    
    # Configura o cabeçalho para texto simples
    headers = {"Content-Type": "text/plain"}  
    
    # Envia a requisição POST
    response = requests.post(url, data=data, headers=headers)
    
    # Mensagens de status para verificar se a conexação foi bem sucedida
    if response.status_code == 200:
        print("Comando enviado com sucesso")
        print("Resposta:", response.text)
    else:
        print("Falha ao enviar o comando")
        print("Status:", response.status_code)
