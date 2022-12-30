@echo off

TITLE grava_todas_dimensoes
SET currentdir=%~dp0
SET kitchen=C:\Program Files\pdi\pentaho-data-integration\Kitchen.bat
SET logfile="%currentdir%log_job_grava_todas_dimensoes.txt"

echo. >> %logfile%
echo. >> %logfile%
"%kitchen%" /file:"C:\Users\LVVE2K631\Documents\4.Projetos_Portifolio\dados_compras_gov_federal\grava_todas_dimensoes.kjb" /level:Basic >> %logfile%
