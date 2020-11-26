import urllib
import requests
import csv
import os
from datetime import datetime
from bs4 import BeautifulSoup

# Classe que representa cada site de notícias que se deseja usar.
# Atributos: Url do site, um vetor com as classes HTML de notícias a obter e os elementos HTML de cada classe (p,h1,h2,...)
class Site:
	# Construtor da classe.
	def __init__(self, url, classesNoticia, elementos):
		self.url = url
		self.classesNoticia = classesNoticia
		self.elementos = elementos
	# Função que obtém as notícias de um site.
	# Input: Se deseja imprimir na tela, se deseja guardar CSV, mais funçoes podem ser adicionadas aqui futuramente.
	def materias(self, imprime = 1, guarda_csv = 1):
		html = obterHTML(self.url) # Faz a requisição do HTML da URL.
		i = 0
		for classe in self.classesNoticia: # Obtém as notícias de cada classe do site.
			obterMaterias(classe, html, self.elementos[i], imprime, guarda_csv)
			i = i + 1

# Função que obtém o HTML a partir de uma URL.
# Input: Uma URL.
# Output: O conteúdo HTML daquela página.
def obterHTML(link):
	conexao = urllib.request.urlopen(link) # Faz a requisição do conteúdo da pagina.
	conteudo = conexao.read().decode("utf8") # Decodifiica o conteúdo da página.
	conexao.close()

	return(conteudo) # Retorna o conteúdo HTML.

# Função que escreve notícias em um arquivo Csv.
# Input: O nome do arquivo a ser escritas as notícias, a data a ser escrita, o título da notícia e o link da notícia.
# Output: Um arquivo csv com o nome desejado criado ou atualizado com as notícias.
def escreveCsv(nomeArquivo, data, titulos, links):
	if (os.path.exists(nomeArquivo) == False): # Se o arquivo ainda não existe,
		with open(nomeArquivo, 'w', newline = '') as arquivo_csv: # Cria o arquivo. 
			escrever = csv.writer(arquivo_csv, delimiter = ';') # Configura a escrita do arquivo.
			escrever.writerow(['Data', 'Titulo', 'Link']) # Escreve o cabeçalho do arquivo.
			for i in range(len(links)): # Para cada notícia,
				escrever.writerow([data, titulos[i].text, links[i]]) # Escreve data, título e link.
				i = i + 1 
	else: # Se o arquivo já existe,
		with open(nomeArquivo, 'a', newline = '') as arquivo_csv: # Abre o arquivo no modo inserir no final.
			escrever = csv.writer(arquivo_csv, delimiter = ';') # Configura a escrita do arquivo.
			for i in range(len(links)):	# Para cada notícia,
				escrever.writerow([data, titulos[i].text, links[i]]) # Escreve data, título e link.
				i = i + 1 

# Função que dado o elemento do título de uma matéria, obtém seu link.
# Input: O elemento do título de uma matéria.
# Output: O link da matéria.
def obterLink(materia):
	pai = materia.parent # Obtém o pai do elemento da matéria.
	while (pai != None) & (pai.name != "a"): # Enquanto não for nulo ou não for o elemento a,
		pai = pai.parent # Avance para o pai deste.
	link = pai['href'] # Quando encontrar o elemento a, obtenha o link no atributo href.
	return link # Retorne o link.

# Função que trata notícias.
# Input: Os títulos das notícias, os links das notícias e booleanos para imprimir na tela ou guardar em csv.
# Output: Notícias tratadas conforme requisições do usuário.
def trataNoticias(titulos, links, imprime, guarda_csv):
	if guarda_csv == 1: # Se deseja guardar Csv.
		now = datetime.now()
		data = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
		escreveCsv("noticias.csv", data, titulos, links) # Passa os dados para a função que escreve csv.
	if imprime == 1: # Se deseja imrpimir na tela,
		now = datetime.now()
		data = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
		for i in range(len(links)): 
			print(data, " ", titulos[i].text, " ", links[i]) # Imprime todas as notícias.

	# Caso o usuário deseje expandir as funcionalidades para notícias, basta seguir o padrão aqui,
	# criando um if se deseja uma função e chamar a função passando os dados. Isso pode ser feito 
	# por exemplo para aplicar algoritmos de Aprendizado de Máquina nas matérias ou simplesmente 
	# obter o conteúdo das matérias.


# Função que obtém os títulos de matéria a partir de um elemento e uma classe em HTML.
# Input: O nome da classe a buscar as notícias, o conteúdo HTML, o elemento a buscar, se imprime e se guarda em csv.
# Output: Obtém os títulos das matérias, seus links e passa essas informações para serem tratadas.
def obterMaterias(nomeClasse, html, elemento, imprime, guarda_csv):
	soup = BeautifulSoup(html, 'html.parser') # Chama o parser HTML.
	materias = soup.find_all(elemento, {'class': nomeClasse}) # Acha os elementos pedidos e dentro desse, as classes pedidas.
	links = []
	for materia in materias: # Para cada matéria encontrada,
		links.append(obterLink(materia)) # Obtém o link da matéria e coloca em um vetor.
	trataNoticias(materias, links, imprime, guarda_csv) # Passa as matérias e os links para serem tratados.

# Para obter as notícias em um site HTML basta criar um elemento da classe Site com o url, um vetor com as classes
# e com os elementos dessa classe. Para as notícias serem tratadas, basta chamar o método materias() com os parâmetros
# que deseja usar para tratar as matérias.

globo = Site('http://globo.com', ['hui-premium__title','hui-highlight-title'], ['p','p']) # Ambas as classes usam o elemento p.
globo.materias()

uol = Site('http://uol.com.br', ['titulo','titulo color2'], ['p','h2']) # Uma classe usa do elemento h2.
uol.materias()