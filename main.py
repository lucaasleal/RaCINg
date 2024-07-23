import pygame
from os.path import join
from random import randint, choice

class Pista(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH / 2, 0))
        self.direction = pygame.math.Vector2(0, 1)
        self.scroll = 800

    def update(self, dt):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.scroll = 1500
        else:
            self.scroll = 800
        self.rect.center += self.direction * dt * self.scroll
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.original_image = pygame.image.load(join('car_6.png')).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 160))
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.rotation = 0
        self.block = 0

    def update(self, dt):
        if (pygame.time.get_ticks() - self.block >= 2999) or (pygame.time.get_ticks() < 2999):
            self.direction.x = int(pygame.key.get_pressed()[pygame.K_d]) - int(pygame.key.get_pressed()[pygame.K_a])
            self.direction = self.direction.normalize() if self.direction else self.direction
        else:
            self.rotation += 120 * dt
            self.image = pygame.transform.rotozoom(self.original_image, self.rotation, 1)
            self.direction.x = 0
        self.rect.center += self.direction * self.speed * dt

class Random(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'car_{randint(0,5)}.png').convert_alpha()
        self.pos = 0
        self.grid = [100, 260, 425, 590]
        self.rect = self.image.get_frect(bottomleft = (choice(self.grid), 0))
        self.direction = pygame.math.Vector2((0, 1))
        self.time_random = pygame.time.get_ticks()
        self.cooldown_duration = 7000
        self.speed = choice([120, 125])

    def update(self, dt):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.speed = choice([225, 235])
        else:
            self.speed = choice([120, 125])
        self.rect.center += self.direction * self.speed * dt
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

class oil(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = (randint(150, 630), 0))
        self.direction = pygame.math.Vector2((0, 1))

    def update(self, dt):
        self.rect.center += self.direction * 800 * dt

def menuzao():
    press = False
    show = True
    flash_timer = 0
    flash_interval = 300
    while not press:
        flash_timer += clock.get_rawtime()

        menutxt = pygame.image.load(join('images', 'menunovao.png'))
        menutxt = pygame.transform.scale(menutxt, (700, 300))
        iniciotxt = pygame.image.load(join('images', 'pressione r.png'))
        iniciotxt = pygame.transform.scale(iniciotxt, (500, 100))
        direitostxt = pygame.image.load(join('images', 'direitos.png'))
        direitostxt = pygame.transform.scale(direitostxt, (659, 22))
        if flash_timer >= flash_interval:
            flash_timer = 0
            show = not show
            display_surface.fill((0, 0, 0))
        if show:
            display_surface.blit(iniciotxt,(145, 500))
        display_surface.blit(menutxt, (45, 80))
        display_surface.blit(direitostxt, (62, 740))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                press = True
                return False
        if pygame.key.get_just_pressed()[pygame.K_r]:
            press = True
            return True
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

def collisions():
    if (pygame.sprite.spritecollide(player, random_sprites, True, pygame.sprite.collide_mask)):
         return True

def difficult(lapse):
    return int(lapse*(4/5))

def import_cars():
    sprite_index = 0
    sprite_corredores = pygame.image.load(join('images', 'spritesheet_oficial.png'))
    sprite_width = sprite_corredores.get_width() // 5
    sprite_height = sprite_corredores.get_height() // 2
    for row in range(2):
        for col in range(5):
            x = col * 112
            y = row * 192
            rect = pygame.Rect(x, y, sprite_width, sprite_height)
            sprite = sprite_corredores.subsurface(rect)
            sprite = pygame.transform.scale(sprite, (79, 130))
            sprite_path = f"car_{sprite_index}.png"
            pygame.image.save(sprite, sprite_path)
            sprite_index += 1


def encerramento():
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    display_surface.fill((0, 0, 0,))
    while True:
        #if pontuacao > HIGHSCORE_label_pontos[-1]:
        #while True:
        '''novorecorde = pygame.image.load('imagensdateladeperdeu/NOVORECORDE.png')]
        color_top = (255, 0, 0)
        color_bottom = (255, 255, 0)

        # escrever aqui o nome do jogador
        texto = render_text_gradient(texto_do_usuario, fonte, color_top, color_bottom)
        for event in pygame.event.get():
            if
        event.type == pygame.QUIT:
        pygame.quit()
        exit()
        HIGHSCORE_label_pontos.pop(-1)
        HIGHSCORE_label_nomes.pop(-1)
        HIGHSCORE_label_pontos.append(pontuacao)
        HIGHSCORE_label_pontos.sort()
        index = HIGHSCORE_label_pontos.index(pontuacao)
        HIGHSCORE_label_nomes.insert(index, nomeplayer)
        # print ranking
        else:'''
        voceperdeu = pygame.image.load('imagensdateladeperdeu/voceperdeu.png')
        voceperdeu = pygame.transform.scale(voceperdeu, (640, 180))
        display_surface.blit(voceperdeu, (80, 180))
        tentardnv = pygame.image.load('imagensdateladeperdeu/pressionerpratentardenovo.png')
        tentardnv = pygame.transform.scale(tentardnv, (500, 70))
        display_surface.blit(tentardnv, (138, 400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                    pass
        pygame.display.update()

#setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 780, 780
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Caxangá Run')
running = True
clock = pygame.time.Clock()
lapse_create = 5000
last_time = pygame.time.get_ticks()

#importações
pista_surf = pygame.image.load(join('images', 'pista.png')).convert_alpha()
import_cars()
oil_surf = pygame.image.load(join('images', 'oil.png')).convert_alpha()

#sprites
all_sprites = pygame.sprite.Group()
background_sprites = pygame.sprite.Group()
oil_sprites = pygame.sprite.Group()
random_sprites = pygame.sprite.Group()
player = Player(all_sprites)

# criando os randoms
random_set = pygame.event.custom_type()
pygame.time.set_timer(random_set, lapse_create)
pista_set = pygame.event.custom_type()
pygame.time.set_timer(pista_set, 500)
oil_set = pygame.event.custom_type()
pygame.time.set_timer(oil_set, 4000)

if menuzao():
    while running:
        dt = clock.tick() / 1000
        '''pontuacao = pygame.time.get_ticks() // 100
        print(pontuacao)'''
        if pygame.time.get_ticks() - last_time > 10000:
            if lapse_create > 1000:
                lapse_create = difficult(lapse_create)
                last_time = pygame.time.get_ticks()
                if lapse_create < 1000:
                    lapse_create = 1000

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == random_set:
                Random((all_sprites, random_sprites))
                pygame.time.set_timer(random_set, lapse_create)
            if event.type == pista_set:
                Pista(pista_surf, background_sprites)
                pygame.time.set_timer(pista_set, 1000)
            if event.type == oil_set:
                oil(oil_surf, oil_sprites)

        # update
        background_sprites.update(dt)
        all_sprites.update(dt)
        oil_sprites.update(dt)
        if collisions():
            running = encerramento()


        # printagem do frame
        display_surface.fill('black')
        background_sprites.draw(display_surface)
        oil_sprites.draw(display_surface)
        all_sprites.draw(display_surface)
        pygame.display.update()

pygame.quit()