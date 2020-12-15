import os
import csv

# Função que escreve notícias em um arquivo Csv.
# Input: O nome do arquivo a ser escritas as notícias, títulos das notícias e os links das notícias.
# Output: Um arquivo csv com o nome desejado criado ou atualizado com as notícias.
def escreve_csv(nomeArquivo, titulos, links):
	if (os.path.exists(nomeArquivo) == False): # Se o arquivo ainda não existe,
		with open(nomeArquivo, 'w', newline = '') as arquivo_csv: # Cria o arquivo. 
			escrever = csv.writer(arquivo_csv, delimiter = ';') # Configura a escrita do arquivo.
			escrever.writerow(['Titulo', 'Link']) # Escreve o cabeçalho do arquivo.
			for i in range(len(titulos)): # Para cada notícia,
				escrever.writerow([titulos[i], links[i]]) # Escreve data, título e link.
	else: # Se o arquivo já existe,
		with open(nomeArquivo, 'a', newline = '') as arquivo_csv: # Abre o arquivo no modo inserir no final.
			escrever = csv.writer(arquivo_csv, delimiter = ';') # Configura a escrita do arquivo.
			for i in range(len(titulos)):	# Para cada notícia,
				escrever.writerow([titulos[i], links[i]]) # Escreve data, título e link.