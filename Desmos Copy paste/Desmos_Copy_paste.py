

import numpy as np
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Desmos Drawer")
image = pygame.image.load("reference_images/diamond ore.png").convert_alpha()
image = pygame.transform.scale(image, (800,600))
    
def draw_lines(array):
    if len(array) % 2 == 0 and not len(array) == 0:
        for i in range(int(len(array) / 2)):
            pygame.draw.line(screen, "WHITE", array[2 * i], array[2 * i + 1], 10)
    elif len(array) % 2 == 1 and not len(array) == 1:
        for i in range(int((len(array) - 1) / 2)):
            pygame.draw.line(screen, "WHITE", array[2 * i], array[2 * i + 1], 10)

        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, "BLUE", array[-1], mouse_pos, 10)
    elif len(array) == 1:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, "BLUE", array[-1], mouse_pos, 10)

def desmos_print(array):
    if len(array) % 2 == 0 and not len(array) == 0:
        for i in range(int(len(array) / 2)):
            c1 = array[2 * i] / max(WIDTH, HEIGHT)
            c2 = array[2 * i + 1] / max(WIDTH, HEIGHT)
            c1[1] *= -1
            c2[1] *= -1
            if c1[0] == c2[0]:
                if c1[1] < c2[1]:
                    print(f"x={c1[0]:.6f} \\left\\{{ {c1[1]:.6f}<y<{c2[1]:.6f} \\right\\}}")
                else:
                    print(f"x={c1[0]:.6f} \\left\\{{ {c2[1]:.6f}<y<{c1[1]:.6f} \\right\\}}")
            else:
                m = (c1[1]-c2[1]) / (c1[0]-c2[0])
                b = c2[1] - m * c2[0]
                if c1[0] < c2[0]:
                    if b > 0:
                        print(f"y={m:.6f}x+{b:.6f} \\left\\{{ {c1[0]:.6f}<x<{c2[0]:.6f} \\right\\}} ")
                    else:
                        print(f"y={m:.6f}x{b:.6f} \\left\\{{ {c1[0]:.6f}<x<{c2[0]:.6f} \\right\\}} ")
                else:
                    if b > 0:
                        print(f"y={m:.6f}x+{b:.6f} \\left\\{{ {c2[0]:.6f}<x<{c1[0]:.6f} \\right\\}} ")
                    else:
                        print(f"y={m:.6f}x{b:.6f} \\left\\{{ {c2[0]:.6f}<x<{c1[0]:.6f} \\right\\}} ")


lines = np.array([])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if len(lines) == 0:
                lines = np.array([mouse_pos])
            else:
                lines = np.vstack((lines, mouse_pos))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print("Copy and paste into desmos to see your work")
                desmos_print(lines)
            elif event.key == pygame.K_e:
                print("Undoed!")
                lines = lines[:-1]

        

    screen.fill("BLACK")
    screen.blit(image, (0,0))
    draw_lines(lines)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()