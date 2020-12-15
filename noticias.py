import sites
from tratarNoticias import trataNoticias

# Para adicionar um site, basta criar uma instância dele e passar seu URL.
globo = sites.Portal("http://globo.com")
# Obter notícias é um método da classe site para obter notícias do portal.
# Para ver quais as opções disponíveis de site, basta indicar com a flag 'Help' 
globo.obterNoticias(['Help'])

# Aqui um exemplo obtendo as notícias em um site que usa HTML e classes. Para este modelo são pedidos
# dois outros argumentos, que são o nome da classe a buscar as notícias e seu tipo. Para outros tipos
# de site, é possível passar outros argumentos, dependendo da implementação..
materias,links = globo.obterNoticias(['HTML-Classes', 'hui-premium__title','p'])

# Com as notícias e links em mãos, a função trataNoticia faz o tratamento adequado com elas de acordo
# com a flag passada. 
trataNoticias(materias,links,0)

# Exemplo com outro site.
uol = sites.Portal("http://uol.com.br")
materias, links = uol.obterNoticias(['HTML-Classes', 'titulo color2','h2'])
trataNoticias(materias,links,1)