import requests
import zipfile
import os
# URL do arquivo
ano = str(input("Informe o ano para baixar os arquivos: (yyyy)"))

for mes in range(1,12):
# Definindo url com mês e ano
    print("Armazenando variável do site")
    ano_mes = "".join([ano,str(mes).zfill(2)])
    url = 'https://portaldatransparencia.gov.br/download-de-dados/compras/{}'.format(ano_mes)
    response = requests.get(url)
    print("Baixando arquivo do ano-mes: " + ano_mes)
    # Faz o download do arquivo
    # Escreve o conteúdo do arquivo em um arquivo local
    print("Armazenando em diretório local")
    with open(ano_mes +'.zip', 'wb') as f:
        f.write(response.content)
    nome_arquivo = ano_mes + '.zip'
    # Abre o arquivo ZIP
    with zipfile.ZipFile(nome_arquivo, 'r') as zip_ref:
        # Extrai todos os arquivos do arquivo ZIP
        zip_ref.extractall()
    # Fecha o arquivo ZIP
    zip_ref.close()
    # Exclui o arquivo ZIP
    os.remove(nome_arquivo)

print("Finalizado")

## Precisa verificar por que não está extraindo os dados de novembro de 2022








