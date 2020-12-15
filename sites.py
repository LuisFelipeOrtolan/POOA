import urllib
import requests
from bs4 import BeautifulSoup

# Função que obtém o HTML a partir de uma URL.
# Input: Uma URL.
# Output: O conteúdo HTML daquela página.
def obterHTML(link):
	conexao = urllib.request.urlopen(link) # Faz a requisição do conteúdo da pagina.
	conteudo = conexao.read().decode("utf8") # Decodifiica o conteúdo da página.
	conexao.close()

	return(conteudo) # Retorna o conteúdo HTML.

# Função que dado o elemento do título de uma matéria, obtém seu link.
# Input: O elemento do título de uma matéria.
# Output: O link da matéria.
def obterLink(materia):
	pai = materia.parent # Obtém o pai do elemento da matéria.
	while (pai != None) & (pai.name != "a"): # Enquanto não for nulo ou não for o elemento a,
		pai = pai.parent # Avance para o pai deste.
	link = pai['href'] # Quando encontrar o elemento a, obtenha o link no atributo href.
	return link # Retorne o link.

# Classe com o portal de notícias.
# Input: Uma Url.
class Portal:
	def __init__(self, url):
		self.url = url

	# Função de obter as notícias de um portal.
	# Input: Uma lista de argumentos, onde o primeiro é o tipo de site e as demais posições são os itens necessários para obter as notícias
	# Output: Um vetor com as machetes e os links das notícias.
	def obterNoticias(self, args):
		if args[0] == 'HTML-Classes':
			html = obterHTML(self.url)
			soup = BeautifulSoup(html, 'html.parser') # Chama o parser HTML.
			links = []
			materias = soup.find_all(args[2], {'class': args[1]}) # Acha os elementos pedidos e dentro desse, as classes pedidas.
			i = 0
			for j in materias:
				materias[i] = j.text # Obtém o texto da manchete.
				links.append(obterLink(j)) # Obtém o link da matéria e coloca em um vetor.
				i = i + 1
			return (materias, links)

		if args[0] == 'Help':
			print("Para obter notícias com HTML em classes use o primeiro argumento como 'HTML Classes', o segundo argumento como o nome da classe e o terceiro o tipo desta classe.")
			return

		# Caso o usuário deseje expandir as funcionalidades de tipos de site, basta seguir o padrão aqui,
		# criando um if se deseja um outro tipo e chamar a função passando os dados.