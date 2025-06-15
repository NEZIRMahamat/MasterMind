import pygame
import sys
from mastermind import generate_random_numbers, compare_user_inputs_solution_game, CHIFFRES, LEN_RANDOM_LIST, ROUND_GAME

WIDTH, HEIGHT = 600, 600
BOX_SIZE = 40
MARGIN = 10

# Couleurs 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
BLUE = (80, 80, 255)
GREEN = (0, 180, 0)
RED = (200, 50, 50)

# Initialisation Pygame 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind - Interface Graphique")
font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 36)

# Fonction qui dessine la grille du jeu
def draw_grid(history, current_guess, round_idx, indices, message_final):
    screen.fill(WHITE)
    #Grille des tentatives
    for row in range(ROUND_GAME):
        for col in range(LEN_RANDOM_LIST):
            x = MARGIN + col * (BOX_SIZE + MARGIN)
            y = 50 + row * (BOX_SIZE + MARGIN)
            pygame.draw.rect(screen, GRAY, (x, y, BOX_SIZE, BOX_SIZE))
            if row < len(history):
                val = history[row][col]
                txt = font.render(str(val), True, BLACK)
                screen.blit(txt, (x + 12, y + 8))
            elif row == round_idx and col < len(current_guess):
                val = current_guess[col]
                txt = font.render(str(val), True, BLUE)
                screen.blit(txt, (x + 12, y + 8))

    #Boutons de chiffres (1 à 6)
    y_btn = 50 + ROUND_GAME * (BOX_SIZE + MARGIN) + 20
    for i, n in enumerate(CHIFFRES):
        x = MARGIN + i * (BOX_SIZE + MARGIN)
        pygame.draw.rect(screen, GRAY, (x, y_btn, BOX_SIZE, BOX_SIZE))
        txt = font.render(str(n), True, BLACK)
        screen.blit(txt, (x + 12, y_btn + 8))
    
    # Indices 
    msg_y = y_btn + BOX_SIZE + 20
    if indices:
        if indices.get("win"):
            txt = big_font.render("Gagné !", True, GREEN)
        else:
            msg = f"-:) {indices['bien']} | X {indices['mal']}"
            txt = font.render(msg, True, RED)
        screen.blit(txt, (MARGIN, msg_y))
    
    if message_final:
        txt = big_font.render(message_final, True, RED if "perdu" in message_final else GREEN)
        screen.blit(txt, (MARGIN, msg_y + 40))

    pygame.display.flip()

# Main du jeu UI
def main():
    secret = generate_random_numbers()
    print("Combinaison secrète :", secret)
    history = []
    current_guess = []
    round_idx = 0
    result = None
    message_final = ""
    running = True

    while running:
        draw_grid(history, current_guess, round_idx, result, message_final)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                y_btn = 50 + ROUND_GAME * (BOX_SIZE + MARGIN) + 20

                if y_btn <= mouse_y <= y_btn + BOX_SIZE:
                    for i, n in enumerate(CHIFFRES):
                        x = MARGIN + i * (BOX_SIZE + MARGIN)
                        if x <= mouse_x <= x + BOX_SIZE:
                            if n not in current_guess and len(current_guess) < LEN_RANDOM_LIST:
                                current_guess.append(n)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(current_guess) == LEN_RANDOM_LIST:
                    well, n_well, lost, n_lost = compare_user_inputs_solution_game(secret, current_guess)
                    history.append(current_guess.copy())
                    result = {"bien": n_well, "mal": n_lost, "win": n_well == LEN_RANDOM_LIST}
                    current_guess = []
                    round_idx += 1
                    if result["win"]:
                        message_final = "Bravo ! Vous avez gagné !"
                        running = False
                    elif round_idx == ROUND_GAME:
                        message_final = f"Vous avez perdu. La combinaison était : {secret}"
                        running = False

                elif event.key == pygame.K_BACKSPACE and current_guess:
                    current_guess.pop()

    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
