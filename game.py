import pygame
pygame.init()

# consts
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
ROCKET_IMG = 'rocket.png'
BALL_IMG = 'ball.png'
BG_COLOR = (64, 64, 64)
# consts

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, width=0, height=0):
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(
        self, image, x=0, y=0, width=0, height=0, speed=5,
        k_up=pygame.K_UP, k_down=pygame.K_DOWN,
    ):
        super().__init__(image, x, y, width, height)
        self.speed = speed

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Пинг Понг')
window.fill(BG_COLOR)
clock = pygame.time.Clock()

game_status = 'game'
while game_status != 'off':
    window.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = 'off'

    clock.tick(60)
    pygame.display.update()

    