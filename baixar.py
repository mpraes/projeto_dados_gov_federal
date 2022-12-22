import requests
import zipfile
import os
# URL do arquivo
print("Armazenando variável do site")
url = 'https://portaldatransparencia.gov.br/download-de-dados/compras/202201'

# Faz o download do arquivo
print("Executando download")
response = requests.get(url)

print("Armazenando em diretório local")
# Escreve o conteúdo do arquivo em um arquivo local
with open('202201.zip', 'wb') as f:
    f.write(response.content)

nome_arquivo = '202201.zip'

# Abre o arquivo ZIP
with zipfile.ZipFile(nome_arquivo, 'r') as zip_ref:
    # Extrai todos os arquivos do arquivo ZIP
    zip_ref.extractall()

# Fecha o arquivo ZIP
zip_ref.close()

# Exclui o arquivo ZIP
os.remove(nome_arquivo)
