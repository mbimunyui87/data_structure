import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Alphabet Reader")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Alphabets
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
current_index = 0

# Cartoon boy image
boy_img = pygame.image.load("boy.png")  # Add the path to your image
boy_rect = boy_img.get_rect(center=(window_width // 2, window_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if boy_rect.collidepoint(event.pos):
                # Check if clicked on the boy
                if current_index < len(alphabets) - 1:
                    current_index += 1
                else:
                    current_index = 0

    # Clear the window
    window.fill(WHITE)

    # Draw alphabets
    alphabet_text = font.render(alphabets[current_index], True, BLACK)
    alphabet_rect = alphabet_text.get_rect(center=(window_width // 2, window_height // 3))
    window.blit(alphabet_text, alphabet_rect)

    # Draw cartoon boy
    window.blit(boy_img, boy_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
