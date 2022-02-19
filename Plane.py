import pygame


def main():
    screen = pygame.display.set_mode((480, 852), 0, 32)

    background = pygame.image.load('a.png').convert()

    while True:
        screen.blit(background, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
