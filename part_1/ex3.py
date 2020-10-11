import pygame
import pygame.draw

pygame.init()

def draw_background():
    """
    Функция рисует фон изображения: ледяной пол, потолок, окно.
    """
    # рисует окно на отделной поверхности, а затем добавляет на соновной экран
    screen_window = pygame.Surface((screen_width, screen_hight))
    screen_window.set_alpha(30)
    screen_window.fill((255, 255, 255, 0))
    pygame.draw.ellipse(screen_window, Yellow, (300, 10, 450, 450), 20)
    pygame.draw.line(screen_window, Yellow, (300, 235), (750, 235), 20)
    pygame.draw.line(screen_window, Yellow, (525, 10), (525, 460), 20)
    # рисует пол и потолок
    pygame.draw.rect(screen, (211, 211, 211, 0), (0, 500, 1000, 500))
    pygame.draw.rect(screen, (135, 206, 235, 0), (0, 0, 1000, 500))
    pygame.draw.line(screen, (0, 0, 0, 0), (0, 500), (1000, 500), 1)
    screen.blit(screen_window, (0, 0))


def draw_fish(position_x: int, position_y: int, size: float,
              surface: pygame.Surface, degree: int):
    """
    Функция рисует рыбину, координаты центра рыбины - это
    соответсвенно position_X (int) и position_y (int).
    Size (float) - это размер рыбы.
    Degree (int) - это угол поворота относительно горизонтали.
    Затем рисунок добавляется на указанную поверхность.
    """
    surface_fish = pygame.Surface((int(2 * size), int(2 * size)),
                                  pygame.SRCALPHA)
    # рисует плавники
    pygame.draw.polygon(surface_fish, Salmon,
                        [(int(size) + int(0.1 * size),
                          int(size) + int(0.2 * size)),
                         (int(size) - int(0.3 * size),
                          int(size) + int(0.1 * size)),
                         (int(size) - int(0.3 * size),
                          int(size) + int(0.3 * size))])
    pygame.draw.polygon(surface_fish, Black,
                        [(int(size) + int(0.1 * size),
                          int(size) + int(0.2 * size)),
                         (int(size) - int(0.3 * size),
                          int(size) + int(0.1 * size)),
                         (int(size) - int(0.3 * size),
                          int(size) + int(0.3 * size))], 1)
    pygame.draw.polygon(surface_fish, Salmon,
                        [(int(size) + int(0.4 * size),
                          int(size) - int(0.2 * size)),
                         (int(size) + int(0.4 * size),
                          int(size) + int(0.1 * size)),
                         (int(size) + int(0.8 * size),
                          int(size) + int(0.2 * size))])
    pygame.draw.polygon(surface_fish, Black,
                        [(int(size) + int(0.4 * size),
                          int(size) - int(0.2 * size)),
                         (int(size) + int(0.4 * size),
                          int(size) + int(0.1 * size)),
                         (int(size) + int(0.8 * size),
                          int(size) + int(0.2 * size))], 1)
    pygame.draw.polygon(surface_fish, Salmon,
                        [(int(size) + int(0.45 * size),
                          int(size) + int(0.6 * size)),
                         (int(size) + int(0.25 * size),
                          int(size) + int(0.1 * size)),
                         (int(size) + int(0.75 * size),
                          int(size) + int(0.2 * size))])
    pygame.draw.polygon(surface_fish, Black,
                        [(int(size) + int(0.45 * size),
                          int(size) + int(0.6 * size)),
                         (int(size) + int(0.25 * size),
                          int(size) + int(0.1 * size)),
                         (int(size) + int(0.75 * size),
                          int(size) + int(0.2 * size))], 1)
    # рисует тело рыбы
    pygame.draw.ellipse(surface_fish, Blue,
                        (int(size), int(size), size, int(0.4 * size)))
    pygame.draw.ellipse(surface_fish, Black,
                        (int(size), int(size), size, int(0.4 * size)), 1)
    # рисует глаз
    pygame.draw.ellipse(surface_fish, Navy,
                        (int(size) + int(0.8 * size),
                         int(size) + int(0.1 * size),
                         int(0.1 * size), int(0.1 * size)))
    pygame.draw.ellipse(surface_fish, Black,
                        (int(size) + int(0.8 * size),
                         int(size) + int(0.1 * size),
                         int(0.1 * size), int(0.1 * size)), 1)
    surface_fish = pygame.transform.rotate(surface_fish, degree)
    surface.blit(surface_fish, (position_x - int(size),
                                position_y - int(size)))


def draw_hole(position_x: int, position_y: int,
              size: float, surface: pygame.Surface):
    """
    Рисует прорубь с центром в точке с координатами position_X (int) и
    position_y (int). Size (float) - это размер проруби.
    Затем рисунок добавляется на указанную поверхностью
    """
    surface_hole = pygame.Surface((int(2 * size), int(2 * size)),
                                  pygame.SRCALPHA)
    pygame.draw.ellipse(surface_hole, (100, 100, 100),
                        (int(size) - int(size / 2),
                         int(size) - int(size / 4),
                         size, int(size / 2)))
    pygame.draw.ellipse(surface_hole, (0, 0, 0),
                        (int(size) - int(size / 2),
                         int(size) - int(size / 4),
                         size, int(size / 2)), 1)
    pygame.draw.ellipse(surface_hole, (0, 128, 128),
                        (int(size) - int(0.4 * size),
                         int(size) - int(0.15 * size),
                         int(0.8 * size), int(0.4 * size)))
    pygame.draw.ellipse(surface_hole, (0, 0, 0),
                        (int(size) - int(0.4 * size),
                         int(size) - int(0.15 * size),
                         int(0.8 * size), int(0.4 * size)), 1)
    surface.blit(surface_hole, (position_x - int(size),
                                position_y - int(size)))


def draw_bear(position_x: int, position_y: int, size: float,
              type: bool, direction: bool):
    """
    Рисует медведя, прорубь и гору рыбы. Центр изображения - это
    position_x (int) и position_y (int). size (float) - это размер изображения.
    type (bool) - отвечает за наличие на рисунке медведя (True - медведь есть,
    False - медведя нет). direction (bool) - отвечает за направление картинки
    (True - направо, False - налево).
    """
    surface_bear = pygame.Surface((int(4 * size), int(4 * size)),
                                  pygame.SRCALPHA)
    # рисует прорубь
    draw_hole(int(2 * size) + int(0.8 * size), int(2 * size) + int(0.2 * size),
              int(0.4 * size), surface_bear)
    # рисует медведя
    if type == True:
        pygame.draw.ellipse(surface_bear, Gray,
                            (int(2 * size) - int(0.25 * size),
                             int(2 * size) - int(0.5 * size),
                             int(0.5 * size), size))
        pygame.draw.ellipse(surface_bear, Black,
                            (int(2 * size) - int(0.25 * size),
                             int(2 * size) - int(0.5 * size),
                             int(0.5 * size), size), 1)
        pygame.draw.ellipse(surface_bear, Gray,
                            (int(2 * size), int(2 * size) + int(size / 4),
                             int(0.4 * size), int(0.3 * size)))
        pygame.draw.ellipse(surface_bear, Black,
                            (int(2 * size), int(2 * size) + int(size / 4),
                             int(0.4 * size), (0.3 * size)), 1)
        pygame.draw.ellipse(surface_bear, Gray,
                            (int(2 * size) + int(0.25 * size),
                             int(2 * size) + int(0.45 * size),
                             int(0.35 * size), int(0.15 * size)))
        pygame.draw.ellipse(surface_bear, Black,
                            (int(2 * size) + int(0.25 * size),
                             int(2 * size) + int(0.45 * size),
                             int(0.35 * size), int(0.15 * size)), 1)
        # рисует руку медведя
        pygame.draw.ellipse(surface_bear, Gray,
                            (int(2 * size) + int(0.15 * size),
                             int(2 * size) - int(0.3 * size),
                             int(0.3 * size), int(0.15 * size)))
        pygame.draw.ellipse(surface_bear, Black,
                            (int(2 * size) + int(0.15 * size),
                             int(2 * size) - int(0.3 * size),
                             int(0.3 * size), int(0.15 * size)), 1)
        # рисует голову
        pygame.draw.ellipse(surface_bear, Gray,
                            (int(2 * size) - int(0.05 * size),
                             int(2 * size) - int(0.65 * size),
                             int(0.45 * size), int(0.25 * size)))
        pygame.draw.ellipse(surface_bear, Black,
                            (int(2 * size) - int(0.05 * size),
                             int(2 * size) - int(0.65 * size),
                             int(0.45 * size), int(0.25 * size)), 1)
        pygame.draw.ellipse(surface_bear, Black,
                            (int(2 * size) + int(0.15 * size),
                             int(2 * size) - int(0.58 * size),
                             int(0.04 * size), int(0.04 * size)))
        pygame.draw.ellipse(surface_bear, Black,
                            (int(2 * size) + int(0.375 * size),
                             int(2 * size) - int(0.55 * size),
                             int(0.04 * size), int(0.04 * size)))
        pygame.draw.arc(surface_bear, Black,
                        (int(2 * size), int(2 * size) - int(0.7 * size),
                         int(0.45 * size), int(0.25 * size)), 4.5, 5.58)
        pygame.draw.ellipse(surface_bear, Gray,
                            (int(2 * size) - int(0.05 * size),
                             int(2 * size) - int(0.65 * size),
                             int(0.08 * size), int(0.08 * size)))
        pygame.draw.ellipse(surface_bear, Black,
                            (int(2 * size) - int(0.05 * size),
                             int(2 * size) - int(0.65 * size),
                             int(0.08 * size), int(0.08 * size)), 1)
        # рисует удочку
        pygame.draw.lines(surface_bear, Black, False,
                          [(int(2 * size) + int(0.32 * size), int(size * 2)),
                           (int(2 * size) + int(0.36 * size),
                            int(2 * size) - int(0.16 * size))], 5)
        pygame.draw.lines(surface_bear, Black, False,
                          [(int(2 * size) + int(0.4 * size),
                            int(2 * size) - int(0.275 * size)),
                           (int(2 * size) + int(0.48 * size),
                            int(2 * size) - int(0.4 * size)),
                           (int(2 * size) + int(0.8 * size),
                            int(2 * size) - int(0.8 * size))], 5)
        pygame.draw.lines(surface_bear, Black, False,
                          [(int(2 * size) + int(0.8 * size),
                            int(2 * size) - int(0.8 * size)),
                           (int(2 * size) + int(0.8 * size),
                            int(2 * size) + int(0.2 * size))], 1)
    # рисует гору рыбы
    draw_fish(int(2 * size) + int(0.8 * size),
              int(2 * size) + int(0.30 * size),
              int(0.2 * size), surface_bear, 0)
    draw_fish(int(2 * size) + int(1 * size),
              int(2 * size) + int(0.1 * size),
              int(0.2 * size), surface_bear, 15)
    draw_fish(int(2 * size) + int(0.8 * size),
              int(2 * size) + int(0.25 * size),
              int(0.2 * size), surface_bear, 30)
    draw_fish(int(2 * size) + int(0.9 * size),
              int(2 * size) + int(0.20 * size),
              int(0.2 * size), surface_bear, 0)
    draw_fish(int(2 * size) + int(1.05 * size),
              int(2 * size) + int(0.23 * size),
              int(0.2 * size), surface_bear, 60)
    # при необходимости разворачивает изображение
    if direction == False:
        surface_bear = pygame.transform.flip(surface_bear, True, False)
        screen.blit(surface_bear, (position_x - int(size),
                                   position_y - int(2 * size)))
    if direction == True:
        screen.blit(surface_bear, (position_x - int(2 * size),
                                   position_y - int(2 * size)))


FPS = 30
Blue = (173, 216, 230)
Black = (0, 0, 0)
Salmon = (250, 128, 114)
Navy = (0, 0, 128)
Yellow = (255, 255, 0)
Gray = (211, 211, 211)
Black = (0, 0, 0)
screen_width = 1000
screen_hight = 1000
BEARS = [[150, 800, 200, True, True], [400, 600, 150, True, False],
         [700, 500, 120, True, True], [700, 700, 300, False, False],
         [150, 600, 100, False, True]]
screen = pygame.display.set_mode((screen_width, screen_hight))
end = pygame.image.load('end.png')
draw_background()
for bear in BEARS:
   draw_bear(bear[0], bear[1], bear[2], bear[3], bear[4])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(end, (0, 0))
            pygame.display.update()
pygame.display.quit()
exit()
pygame.quit()
