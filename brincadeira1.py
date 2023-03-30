''' fazer codigo matrix'''

import pygame
import random

pygame.init()

# Definindo as dimensões da tela
width, height = 640, 480
#width, height = 800, 600
screen = pygame.display.set_mode((width, height))
#screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


# Definindo a lista de caracteres
chars = "0123456789"
chars = [char for char in chars]

# Definindo a fonte
font_size = 20
font = pygame.font.SysFont("monospace", font_size)

# Classe para representar cada caractere na tela
class Character:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.char = random.choice(chars)
        self.color = (0, 255, 0) # Cor verde

    def draw(self, surface):
        text = font.render(self.char, True, self.color)
        surface.blit(text, (self.x, self.y))

    def update(self):
        self.y += self.speed
        if self.y > height:
            self.y = -font_size # Começa do topo novamente
            self.char = random.choice(chars) # Escolhe um novo caractere aleatoriamente

# Cria a lista de caracteres
n_chars = 50 # Número de caracteres na tela
characters = [Character(random.randint(0, width), random.randint(0, height), 0.5) for i in range(n_chars)]

# Loop principal do programa
while True:
    # Verifica se o usuário quer sair
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Pinta a tela de preto
    screen.fill((0, 0, 0))

    # Desenha e atualiza cada caractere
    for char in characters:
        char.draw(screen)
        char.update()

    # Atualiza a tela
    pygame.display.flip()
