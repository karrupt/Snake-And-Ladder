# importing the pygame module along with other modules
import pygame
import random
from pygame import mixer
# ----------------------------------------------------------------------------------------------------------------------
# initialising the pygame module
pygame.init()
game_screen = pygame.display.set_mode((900, 700)) # creating a gamescreen of 900 * 700 pixels
game_state = "running"
# setting the caption and icon - this will be displayed in the top left corner of the window
pygame.display.set_caption("Snake & Ladder")
icon = pygame.image.load("snake and ladder icon.png")
pygame.display.set_icon(icon)
# setting the background image
background_image = pygame.image.load("snake and ladder board.jpg")
# arrow that point to the current player playing900, 700
arrow = pygame.image.load("arrow.png")
# players are global so we can use them from anywhere
# global player1, player2
player1 = 0
player2 = 0
# dictionary of where sankes and ladder are
snake = {51: 11, 56: 15, 62: 57, 92: 53, 98: 8} # key represent head of snake and corresponding value represent its tail
ladder = {2: 38, 4: 14, 9: 31, 33: 85, 52: 88, 80: 99} # key,value pair represents bottom and top of ladder respectively
# ----------------------------------------------------------------------------------------------------------------------
# loading the dice onto the display
def throw_dice():
    dice_roll = mixer.Sound('dice_roll.mp3') # whenever dice is rolled this sound plays
    dice_roll.play()
    num = random.randint(1, 6)
    if num == 1:
        dice = pygame.image.load("1.png")
    elif num == 2:
        dice = pygame.image.load("2.png")
    elif num == 3:
        dice = pygame.image.load("3.png")
    elif num == 4:
        dice = pygame.image.load("4.png")
    elif num == 5:
        dice = pygame.image.load("5.png")
    elif num == 6:
        dice = pygame.image.load("6.png")
    return (dice, num)
# ----------------------------------------------------------------------------------------------------------------------
# ______________________________________________________________________________________________________________________
# this will display player 1 and player 2 at the corresponding locations
def display_players_text():
    # setting up the players
    p1 = pygame.font.Font("freesansbold.ttf", 32)
    p2 = pygame.font.Font("freesansbold.ttf", 32)
    p1_text = p1.render("PLAYER 1", True, (255, 0, 0))
    p2_text = p2.render("PLAYER 2", True, (0, 0, 255))
    game_screen.blit(p1_text, (745, 420)) # blit helps is displaying onto the screen i.e. blitting
    game_screen.blit(p2_text, (745, 560))
# ----------------------------------------------------------------------------------------------------------------------
# ______________________________________________________________________________________________________________________
# arrow shows the current player playing
def show_arrow(chance):
    if chance == 0:
        game_screen.blit(arrow, (705, 420))
    if chance == 1:
        game_screen.blit(arrow, (705, 560))
# ----------------------------------------------------------------------------------------------------------------------
# ______________________________________________________________________________________________________________________
# where to move a player onto the screen
def move_on_board(player_number, direc, x, y):  # need to return x and y coordinate of player
    if player_number == 1:
        if direc == "left":
            x -= 70
        elif direc == "right":
            x += 70
        elif direc == "up":
            y -= 70
        elif direc == "down":  # down
            y += 70
        return x, y
    if player_number == 2:
        if direc == "left":
            x -= 70
        elif direc == "right":
            x += 70
        elif direc == "up":
            y -= 70
        elif direc == "down":  # down
            y += 70
        return x, y
# ______________________________________________________________________________________________________________________
# showing the players
def show_current_players(p_img, px1, py1, px2, py2):
    game_screen.blit(player_img[0], (px1, py1))
    game_screen.blit(player_img[1], (px2, py2))
# ----------------------------------------------------------------------------------------------------------------------
# creating a list which helps us to choose between directions
dir = []
j = 0
for i in range(10):
    if (j // 10) % 2 == 0:
        dir.append([j + 1, j + 10, "right", "left"])
    else:
        dir.append([j + 1, j + 10, "left", "right"])
    j += 10

# ______________________________________________________________________________________________________________________
# moving the player on the board and return the x and y coordinate of the player to be  moved
def move_player(player_no, count,
                ls_cord):  # count can be +ve as well as -ve depending upon whether player wants to move ahead or behind
    # ls_cord = [px1, py1, px2, py2]
    if count == 0:
        if player_no == 1:
            return ls_cord[0], ls_cord[1]
        if player_no == 2:
            return ls_cord[2], ls_cord[3]
    global dir
    global player1, player2
    if player_no == 1:
        if count < 0:
            # can move in "left, right or down" direction
            while count != 0:
                direction = "----"
                if (player1 % 10) == 1:
                    direction = "down"
                else:
                    for i in range(10):
                        if player1 <= dir[i][1]:
                            direction = dir[i][3]
                            break

                print(direction, end=" ")
                ls_cord[0], ls_cord[1] = move_on_board(1, direction, ls_cord[0], ls_cord[1])  # left right or down
                player1 -= 1
                count += 1
            print()
            return ls_cord[0], ls_cord[1]
        else:  # for count > 0
            if player1 + count > 100:
                return ls_cord[0], ls_cord[1]
            while count != 0:
                direction = "----"
                if (player1 % 10) == 0:
                    direction = "up"
                else:
                    for i in range(10):
                        if player1 < dir[i][1]:
                            direction = dir[i][2]
                            break
                print(direction, end=" ")
                ls_cord[0], ls_cord[1] = move_on_board(1, direction, ls_cord[0], ls_cord[1])  # left right or up
                player1 += 1
                count -= 1
            print()
            return ls_cord[0], ls_cord[1]

    else:  # for player no. 2
        if count < 0:
            # "left, right or down"
            while count != 0:
                direction = "----"
                if (player2 % 10) == 1:
                    direction = "down"
                else:
                    for i in range(10):
                        if player2 <= dir[i][1]:
                            direction = dir[i][3]
                            break
                print(direction, end=" ")
                ls_cord[2], ls_cord[3] = move_on_board(2, direction, ls_cord[2], ls_cord[3])  # left right or up
                player2 -= 1
                count += 1
            print()
            return ls_cord[2], ls_cord[3]

        else:
            if player2 + count > 100:
                return ls_cord[2], ls_cord[3]
            # left right or up
            while count != 0:
                direction = "----"
                if (player2 % 10) == 0:
                    direction = "up"
                else:
                    for i in range(10):
                        if player2 < dir[i][1]:
                            direction = dir[i][2]
                            break
                print(direction, end=" ")
                ls_cord[2], ls_cord[3] = move_on_board(2, direction, ls_cord[2], ls_cord[3])  # left right or up
                player2 += 1
                count -= 1
            print()
            return ls_cord[2], ls_cord[3]
# ----------------------------------------------------------------------------------------------------------------------
# ______________________________________________________________________________________________________________________
# creating a button which will be pressed to invoke throw_dice() function
button = pygame.Rect(720, 200, 152, 62)
button_img = pygame.image.load("throw_dice.png")
DICE, num = pygame.image.load("1.png"), 1
chance = 0  # initially first player will have the chance to play the game:      0-> first    1->second
continuous_chances = 0  # player can play maximum of 3 changes in a row under certain condition
current_sum = 0 # maximum sum can be 17
player_img = [pygame.image.load("player1.png"), pygame.image.load("player2.png")]
on_the_board = [False, False]  # are players on the board?
px1 = 750
py1 = 350
px2 = 750
py2 = 600
player1_wins = False
player2_wins = False
player1_wins_font = pygame.font.Font("freesansbold.ttf", 70)
player2_wins_font = pygame.font.Font("freesansbold.ttf", 70)
player1_wins_text = player1_wins_font.render(" PLAYER 1 WON !!! ", True, (45, 117, 113))
player2_wins_text = player2_wins_font.render(" PLAYER 2 WON !!! ", True, (45, 117, 113))
snake_bite_font = pygame.font.Font("freesansbold.ttf", 64)
snake_bite_text = snake_bite_font.render("! ! Snake Bite ! !", True, (255, 0, 0))
ladder_font = pygame.font.Font("freesansbold.ttf", 64)
ladder_up_text = ladder_font.render(" ! ! LADDER UP ! !", True, (0, 255, 0))
snake_bite = False
ladder_up = False
# ----------------------------------------------------------------------------------------------------------------------
while game_state == "running":
    # filling the background color
    game_screen.fill((240, 240, 240))
    # setting the background image
    game_screen.blit(background_image, (0, 0))  # game board

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = "stop"
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() # return the x,y coordinate where mouse is pressed
            if button.collidepoint(mouse_pos):
                (DICE, num) = throw_dice()
                if num == 6 and continuous_chances == 0:  # meaning current is not the third chance and you got a 6
                    continuous_chances = 1
                    current_sum = 6
                elif num == 6 and continuous_chances == 1:  # meaning current is not the third chance and you got a 6
                    continuous_chances = 2
                    current_sum = 12
                elif num == 6 and continuous_chances == 2:  # meaning current is the third chance and you got a 6
                    current_sum = 0
                    continuous_chances = 0
                    print(1 + chance, current_sum)
                elif num != 6 and continuous_chances != 0: # means its not your first chance and you got a non 6 number
                    current_sum += num
                    continuous_chances = 0
                    # print(1 + chance, current_sum)
                elif num != 6 and continuous_chances == 0: # means its your first chance and you got non 6 number
                    current_sum = num
                    continuous_chances = 0
                    # print(1 + chance, current_sum)
                # curr_sum = 0
                # while True:
                #     if curr_sum==18:
                #         curr_sum=0
                #         break
                #     if num!=6:
                #         curr_sum+=num
                #         break
                #     curr_sum+=6

                # this means current player 1 is on the board and is ready to move (not in middle of throwing dice)
                if chance == 0 and on_the_board[chance] == True and continuous_chances == 0:
                    px1, py1 = move_player(1, current_sum, [px1, py1, px2, py2])
                    if player1 == 100:
                        player1_wins = True
                        winning = mixer.Sound("winning_sound.mp3")
                        winning.play()
                        break
                    current_sum = player1
                    #  if there is snake bite for player 1
                    if player1 in snake.keys():
                        danger_snake = mixer.Sound('snake_bite_danger.mp3')
                        danger_snake.play()
                        snake_bite = True
                        print("snake bite for player 1 at pos " + str(current_sum))
                        # print(snake[player1] - current_sum)
                        # print("before = ", px1, py1)
                        px1, py1 = move_player(1, snake[player1] - current_sum, [px1, py1, px2, py2])
                        # print("after = ", px1, py1)
                        # print(player1)
                    else:
                        snake_bite = False
                    # if there is ladder up for player 1
                    if player1 in ladder.keys():
                        ladder_sound = mixer.Sound('ladder_up.mp3')
                        ladder_sound.play()
                        px1, py1 = move_player(1, ladder[player1] - current_sum, [px1, py1, px2, py2])
                        ladder_up = True
                    else:
                        ladder_up = False
                    current_sum = 0

                # this means current player 2 is on the board and is ready to move (not in middle of throwing dice)
                elif chance == 1 and on_the_board[chance] == True and continuous_chances == 0:
                    px2, py2 = move_player(2, current_sum, [px1, py1, px2, py2])
                    if (player2 == 100):
                        player2_wins = True
                        winning = mixer.Sound("winning_sound.mp3")
                        winning.play()
                        break
                    current_sum = player2
                    # if there is a snake bite for player 2
                    if player2 in snake.keys():
                        snake_bite = True
                        danger_snake = mixer.Sound('snake_bite_danger.mp3')
                        danger_snake.play()
                        print("snake bite for player 2 at pos " + str(current_sum))
                        print(snake[player2] - current_sum)
                        print("before = ", px2, py2)
                        px2, py2 = move_player(2, snake[player2] - current_sum, [px1, py1, px2, py2])
                        print("after = ", px2, py2)
                        print(player2)
                        if player2 == 100:
                            player2_wins = True
                            break
                    else:
                        snake_bite = False
                    # if there is ladder present for player 2
                    if player2 in ladder.keys():
                        ladder_sound = mixer.Sound('ladder_up.mp3')
                        ladder_sound.play()
                        px2, py2 = move_player(2, ladder[player2] - current_sum, [px1, py1, px2, py2])
                        ladder_up = True
                    else:
                        ladder_up = False
                    current_sum = 0
        if event.type == pygame.MOUSEBUTTONUP:
            # moving for the first time from the side line to numerical value 1
            # the player is not on the board and current sum is greter than 6 but not 12 or 18
            if current_sum > 6 and current_sum % 6 != 0 and on_the_board[chance] == False:
                current_sum -= 6
                #  for player 1
                if chance == 0:
                    player1 = 1
                    px1 = 10
                    py1 = 630
                    px1, py1 = move_player(1, current_sum, [px1, py1, px2, py2])
                    if player1 in ladder.keys():
                        ladder_sound = mixer.Sound('ladder_up.mp3')
                        ladder_sound.play()
                        px1, py1 = move_player(1, ladder[player1] - player1, [px1, py1, px2, py2])
                        ladder_up = True
                    else:
                        ladder_up = False
                #  for player 2
                else:
                    player2 = 1
                    px2 = 10
                    py2 = 655
                    px2, py2 = move_player(2, current_sum, [px1, py1, px2, py2])
                    if player2 in ladder.keys():
                        ladder_sound = mixer.Sound('ladder_up.mp3')
                        ladder_sound.play()
                        px2, py2 = move_player(2, ladder[player2] - player2, [px1, py1, px2, py2])
                        ladder_up = True
                    else:
                        ladder_up = False
                on_the_board[chance] = True
            # changing the chance of the player
            if num == 6 and continuous_chances == 0:  # meaning current is the third chance and you got a 6
                chance = 1 - chance
                break
            elif num != 6:
                chance = 1 - chance
                break
    # if no one has won
    if player1_wins == False and player2_wins == False:
        display_players_text()
        game_screen.blit(button_img, (720, 200))
        show_arrow(chance)
        game_screen.blit(DICE, (740, 60))
        if snake_bite:
            game_screen.blit(snake_bite_text, (200, 300))
        if ladder_up:
            game_screen.blit(ladder_up_text, (200, 300))
        show_current_players(player_img, px1, py1, px2, py2)
    #  if player 1 has won
    elif player1_wins == True:
        game_screen.blit(player1_wins_text, (100, 200))
    # if p
    else:
        game_screen.blit(player2_wins_text, (100, 200))

    pygame.display.update()
