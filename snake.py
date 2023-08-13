import pygame
import os

"""
 Initialize the game
"""
pygame.init()

"""
 Height and Width
"""
HEIGHT = 600
WIDTH = 800
STARTING_POS = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
"""
 FPS - To stabiliize the game
 The loop would be running differently on each computer, based on the speed 
 To control how fast the game is running, we set a FPS 
"""
FPS = 60

"""
 Window Name
"""
pygame.display.set_caption("Snake AI")

"""
 Create a screen
"""
screen = pygame.display.set_mode((WIDTH, HEIGHT))

"""
 Loading the sprites
 The reason why we lose os directory instead of writing the enriew path is because
   the directory system may be different on different operating systems 
 The variables defined below are now called "surfaces" as per pygame
"""
HEAD = pygame.image.load(os.path.join("Graphics", "head_right.png"))
BODY = pygame.image.load(os.path.join("Graphics", "body_horizontal.png"))
TAIL = pygame.image.load(os.path.join("Graphics", "tail_left.png"))

"""
 Background color in RGB
 Must be a tuple
"""
BACKGROUND = (0, 0, 0)


def draw_to_window():
    """
    This function fills the background
    """
    screen.fill(BACKGROUND)

    """
     This function draws surfaces to the display
     Note on the pygame coordinate system:
        (0,0) is in the top left
    """
    screen.blit(HEAD, STARTING_POS)  # (400, 300))

    """
     After drawing anythign we need to update the screen
     Can also pass an argument to update a portion of the screen
     Passing no argumments updates the entire screen (same as pygame.display.flip())
     https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip
    """
    pygame.display.update()


def main():
    """ """
    head = pygame.Rect(WIDTH / 2, HEIGHT / 2, 40, 40)
    # body = pygame.Rect()
    """
    This clock ensures we run the while loops FPS times per second
    Given that the machine can reach the FPS value
    """
    clock = pygame.time.Clock()

    """
     Set the game as running
    """
    running = True

    """
     We quit the game if the event is of quit type
    """
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_to_window()

    """
     If the event is quit, the loop ends and the game quits  
    """
    pygame.quit()


if __name__ == "__main__":
    main()
