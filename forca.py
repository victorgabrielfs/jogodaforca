# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
import operator
from functools import reduce

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.letrasCorretas = []
		self.letrasErradas = []
		self.hiddenWord = []

	# Método para adivinhar a letra
	def guess(self):
		not_ok = True
		while not_ok:
			letra = input("Digite uma letra: ")
			if len(letra.strip()) > 1:
				print("Digite uma letra, não mais que isso")
			elif letra.strip() in self.letrasCorretas or letra in self.letrasErradas:
				print("Você já usou essa letra, tente de novo")
			else:

				if letra in self.word:
					self.letrasCorretas.append(letra)
				else:
					self.letrasErradas.append(letra)
				not_ok = False
		
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if len(list(filter(lambda x: x in self.letrasCorretas, self.word))) == len(self.word) or len(self.letrasErradas) == 6:
			return True
		else:
			return False
		
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):

		if len(list(filter(lambda x: x in self.letrasCorretas, self.word))) == len(self.word):
			return True
		else:

			return False

		

	# Método para não mostrar a letra no board
	def hide_word(self):
		self.hiddenWord.clear()
		for letra in self.word:
			if letra in self.letrasCorretas:
				self.hiddenWord.append(letra)
			else:
				self.hiddenWord.append("_")





		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.letrasErradas)], "\n")
		print("Palavra: ",  reduce(operator.add, self.hiddenWord), "\n")
		print("Letras erradas: ", str(self.letrasErradas).strip("[]"), "\n")
		print("Letras corretas: ", str(self.letrasCorretas).strip("[],"), "\n","\n")

# Função para ler uma palavra de forma aleatória do banco de palavras


def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():
		# Verifica o status do jogo
		game.hide_word()
		game.print_game_status()
		game.guess()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		game.hide_word()
		game.print_game_status()
		print ('\nParabéns! Você venceu!!')
	else:
		game.hide_word()
		game.print_game_status()
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa


if __name__ == "__main__":
	main()

