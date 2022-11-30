import pygame
import sys
from bullet import Bullet
from enemies import Enemy
import time


# The controller file is the second most important file in the game.
# It describes all the functions and actions of the game and for each
# of its components

# The events function is named as it should be understood.
# All events related to the use of the keyboard and
# mouse by the user are described here.
def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # movement of the gun to the right on the button D
            if event.key == pygame.K_d:
                gun.mright = True
            # movement of the gun to the left on the button A
            elif event.key == pygame.K_a:
                gun.mleft = True
            # Shooting from a gun on a button SPACE
            elif event.key == pygame.K_SPACE:
                # Each shot creates a new bullet object.
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Gun movement stop right
            if event.key == pygame.K_d:
                gun.mright = False
            # Gun movement stop left
            elif event.key == pygame.K_a:
                gun.mleft = False


# Screen drawing function...
def update(bg_color, screen, stats, scores, gun, army, bullets):
    # ...background
    screen.blit(bg_color, (0, 0))
    # ...points
    scores.show_score()
    # ... bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # ... guns
    gun.output()
    # ...and armies of enemies
    army.draw(screen)
    pygame.display.flip()


# Function by producing the main battle music
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('Music/It Hat to be This Way.mp3 ')
    # Endless music playback
    pygame.mixer.music.play(-1)
    # Change the music volume (can be changed from 0 to 1)
    pygame.mixer.music.set_volume(0.1)


# Function for bullet actions
def update_bullets(screen, stats, scores, army, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Creating a collision between a bullet and an alien
    collisions = pygame.sprite.groupcollide(bullets, army, True, True)
    # If a bullet hits an alien...
    if collisions:
        for army in collisions.values():
            # ...the player gets 10 points for killing an enemy
            stats.score += 10 * len(army)
        # Display points and lives
        scores.image_score()
        check_best_score(stats, scores)
        scores.image_guns()
    # If the aliens run out, a new army of enemies is created
    if len(army) == 0:
        bullets.empty()
        create_army(screen, army)


# Gun destroy function
def kill_gun(stats, screen, scores, gun, army, bullets):
    # If the enemies touched the cannon or reached the end of the path...
    # ...if there is still health
    if stats.guns_left > 0:
        # ...1 health is taken away
        stats.guns_left -= 1
        # updated gameplay:
        scores.image_guns()
        # old army removed
        army.empty()
        # bullets removed
        bullets.empty()
        # new army created
        create_army(screen, army)
        # new gun created
        gun.create_gun()
        time.sleep(1)
    else:
        # Otherwise, the player has completely lost and the game ends.
        stats.run_game = False
        sys.exit()


# Function for army actions
def update_army(stats, screen, scores, gun, army, bullets):
    army.update()
    # If there was a collision between the gun and the enemy
    if pygame.sprite.spritecollideany(gun, army):
        # the army can destroy the cannon
        kill_gun(stats, screen, scores, gun, army, bullets)
    # ...or win by reaching the end of the screen
    check_position(stats, screen, scores, gun, army, bullets)


# Enemy Position Recognition Function
def check_position(stats, screen, scores, gun, army, bullets):
    screen_rect = screen.get_rect()
    for enemies in army.sprites():
        # If at least one of the enemy army has reached the bottom of the screen:
        if enemies.rect.bottom >= screen_rect.bottom:
            # the gun is destroyed and the next attempt begins or the game ends
            kill_gun(stats, screen, scores, gun, army, bullets)
            break


# Function to create a new army
def create_army(screen, army):
    enemies = Enemy(screen)
    # The size of each enemy is calculated and how many enemies will be horizontally...
    enemy_width = enemies.rect.width
    numbers_enemy_x = int((700 - 2 * enemy_width) / enemy_width)
    # ...and vertically
    enemy_height = enemies.rect.height
    numbers_enemy_y = int((800 - 100 - 2 * enemy_height) / enemy_height)
    # When one alien has been calculated, there are two cycles,
    # both of which will create enemies vertically and horizontally
    for row_number in range(numbers_enemy_y - 4):
        for enemy_number in range(numbers_enemy_x):
            enemies = Enemy(screen)
            enemies.x = enemy_width + enemy_width * enemy_number
            enemies.y = enemy_height + enemy_height * row_number
            enemies.rect.x = enemies.x
            enemies.rect.y = enemies.rect.height + enemies.rect.height * row_number
            # In the end, we all unite into a single army
            army.add(enemies)


# Function for identifying the best score
def check_best_score(stats, scores):
    # If the score of the current game is better than the best score...
    if stats.score > stats.high_score:
        # ...then the current score becomes the best
        stats.high_score = stats.score
        scores.image_high_score()
        with open('TheBestScore', 'w') as f:
            f.write(str(stats.high_score))
