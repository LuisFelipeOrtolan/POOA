import csv_not

# Função que trata notícias.
# Input: Os títulos das notícias, os links das notícias e um inteiro que indica o método de tratamento das notícias.
# Output: Notícias tratadas conforme requisição do usuário.
def trataNoticias(materia, link, opcao):

	if opcao == 0:
		for i in range(len(materia)):
			print("Titulo da materia: ", materia[i])
			print("Link da materia: ", link[i])
	elif opcao == 1:
		#for i in range(len(materia)):
			#print(materia[i], '\n', link[i],'\n')
		csv_not.escreve_csv("materia.csv", materia, link)

	else:
		print("Opcao invalida. Use a opcao zero para imprimir na tela, um para guardar em um arquivo csv.")

	# Caso o usuário deseje expandir as funcionalidades para notícias, basta seguir o padrão aqui,
	# criando um if se deseja uma função e chamar a função passando os dados. Isso pode ser feito 
	# por exemplo para aplicar algoritmos de Aprendizado de Máquina nas matérias ou simplesmente 
	# obter o conteúdo das matérias.