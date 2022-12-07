import pygame

# The class GameMenu was created to describe the structure of the game menu

# Let's create a global variable for more convenient work with functions

# According to PEP8 standards, colors should be specified
# at the very beginning of the file, and then work with them
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
yellow_red = (232, 69, 69)
green_sosna = (13, 115, 119)
green = (0, 255, 0)
blue = (50, 153, 213)
dark_blue = (43, 46, 74)
orange = (255, 165, 0)
violet = (238, 130, 238)
gray = (50, 50, 50)
lime = (0, 255, 0)
indigo = (75, 0, 130)
golden = (218, 165, 32)
firered = (178, 34, 34)

# Create objects for rendering text
pygame.font.init()
font_style = pygame.font.SysFont('bahnschrift', 20)
score_font = pygame.font.SysFont('comicsansms', 20)
menu_style = pygame.font.SysFont('arial', 45)

# Button border color and menu background music
color_rect = gray
bg_menu = pygame.image.load('Image/menu_fon.png')


# The function of drawing two buttons: "Новая игра" and "Выход".
# The first button starts the game itself, the second allows you to exit the game
def screen_menu(screen):
    # Button rendering
    pygame.draw.rect(screen, color_rect,
                     (230, 250, 250, 70), 4)
    pygame.draw.rect(screen, color_rect,
                     (230, 350, 250, 70), 4)
    # Drawing text on buttons
    message = menu_style.render("Новая игра", True, green_sosna)
    screen.blit(message, [255, 255])
    message = menu_style.render("Выйти", True, yellow_red)
    screen.blit(message, [300, 355])


# The main function of this file. To begin with,
# we introduce three global variables through which it will be easier to work
def menu_control(screen):
    menu = True
    pygame.mouse.set_visible(True)
    while menu:
        # Menu drawing
        screen.blit(bg_menu, (0, 0))
        screen_menu(screen)
        pygame.display.update()
        for event in pygame.event.get():
            # Mouse interaction through the cursor with the buttons in the menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Button selection "Новая игра"
                    x, y = pygame.mouse.get_pos()
                    if (x > 230) and (x < 470) and (y > 250) and (y < 320):
                        menu = False
                        # Button selection "Выход"
                    elif (x > 230) and (x < 470) and (y > 350) and (y < 420):
                        exit()


# Function for the operation of music in the menu
def music_in_menu():
    pygame.mixer.init()
    pygame.mixer.music.load('Music/menu_music.mp3 ')
    # Endless music playback
    pygame.mixer.music.play(-1)
    # Change the music volume (can be changed from 0 to 1)
    pygame.mixer.music.set_volume(0.2)
