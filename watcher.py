import time
import os
import yaml
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from python_requests import request

# Diretórios e arquivos
image_dir = 'images-dst/'
yaml_file = 'yaml-dst/status.yaml'

# Função para ler o arquivo YAML
def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Função para apagar todos os arquivos em um diretório
def delete_files_in_directory(directory):
    print(f"Apagando arquivos no diretório: {directory}")
    files = os.listdir(directory)
    for filename in files:
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

# Função para exibir uma mensagem no terminal
def show_message():
    print("A aquisição de imagens está completa. Realizando inferências e apagando imagens...")

# Função para contar arquivos em um diretório
def count_files_in_directory(directory):
    return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

# Classe para lidar com eventos de sistema de arquivos
class DirectoryWatchHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Verifica se o arquivo YAML foi alterado
        if event.src_path == yaml_file.replace('/', '\\'):
            # Lê a variável do arquivo YAML
            try:
                data = read_yaml(yaml_file)
                inference = data.get('inference', False)

                if inference:
                    print("Processando...")
                    ######################################
                    # CHAMADA DO SCRIPT DE ANÁLISE DE PLACA
                    results = ['BCV6189', 'OFG4563']
                    set_result = results[0]
                    print(f"Leitura da Placa: {set_result}")
                    if set_result == results[0]:
                        request.send_command(is_approved = 1)
                    else:
                        request.send_command(is_approved = 0)
                    ######################################

                    # Apaga imagens
                    delete_files_in_directory(image_dir)
                else:
                    print("Iniciando Aquisição das Imagens...")
            except Exception as e:
                print(f"Erro ao ler o arquivo YAML: {e}")

# Função para monitorar o diretório e mostrar status a cada 5 segundos
def monitor_status():
    while True:
        time.sleep(1)
        num_files = count_files_in_directory(image_dir)
        if num_files == 0:
            pass
            # print(f"O diretório {image_dir} está vazio.")
        else:
            print(f"Status: {num_files} imagens no diretório {image_dir}.")

# Configuração do observador
event_handler = DirectoryWatchHandler()
observer = Observer()
observer.schedule(event_handler, path=os.path.dirname(yaml_file), recursive=False)  # Monitorar o diretório do arquivo YAML
observer.start()

print("Iniciando monitoramento...")

try:
    monitor_status()
except KeyboardInterrupt:
    print("Monitoramento interrompido pelo usuário.")
    observer.stop()
observer.join()
