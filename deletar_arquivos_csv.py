import requests
import zipfile
import os
# URL do arquivo
ano = str(input("Informe o ano que deseja baixar os arquivos: "))

for mes in range(1,12):
    #Criando variáveis para os quatro nomes possíveis de arquivos diferentes por mês e ano
    ano_mes_item_compra = "".join([ano,str(mes).zfill(2),'_ItemCompra.csv'])
    ano_mes_termo = "".join([ano,str(mes).zfill(2),'_TermoAditivo.csv'])
    ano_mes_apostilamento = "".join([ano,str(mes).zfill(2),'_Apostilamento.csv'])
    ano_mes_compras = "".join([ano,str(mes).zfill(2),'_Compras.csv'])   
    file_names = [ano_mes_item_compra, ano_mes_termo, ano_mes_apostilamento, ano_mes_compras]
    # Verifica se os arquivo existem no diretorio local para deletar
    for file_name in file_names:
        # Verifica se o arquivo existe
        if os.path.exists(file_name):
            # Deleta o arquivo
            os.remove(file_name)
            # Confirma deleção do arquivo, caso existente
            print(f"O arquivo {file_name} foi deletado com sucesso.")
        else:
            print(f"O arquivo {file_name} não foi encontrado.")


