import requests
import zipfile
import os
# URL do arquivo
ano = str(input("Informe o ano e mês desta maneira: (yyyy)"))


for mes in range(1,12):
# Definindo url com mês e ano
    print("Armazenando variável do site")
    mes_ano = "".join([ano,str(mes).zfill(2)])
    url = 'https://portaldatransparencia.gov.br/download-de-dados/compras/{}'.format(mes_ano)
    response = requests.get(url)
    with open(mes_ano +'.zip', 'wb') as f:
        f.write(response.content)
    nome_arquivo = mes_ano + '.zip'
    # Abre o arquivo ZIP
    with zipfile.ZipFile(nome_arquivo, 'r') as zip_ref:
        # Extrai todos os arquivos do arquivo ZIP
        zip_ref.extractall()

# Faz o download do arquivo
print("Executando download")


print("Armazenando em diretório local")

# Escreve o conteúdo do arquivo em um arquivo local


# Fecha o arquivo ZIP
zip_ref.close()

# Exclui o arquivo ZIP
os.remove(nome_arquivo)
