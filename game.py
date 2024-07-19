"""
Creator: mashaahsam
Started Project: 2024-07-18

RegularJoe will be a text-based clicking game where the character is a Regular 
person just trying to get by. With a potential twist coming soon...
"""

## Installs / Imports
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button-based Story Game")


## CLASSES

# Button class
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)


## FUNCTIONS

# Draw the home screen
def draw_home_screen():
    screen.fill((173, 216, 230))  # Light blue background
    buttons = [
        Button("Bathroom", 50, 50, 200, 50, lambda: go_to_location("bathroom")),
        Button("Bedroom", 50, 150, 200, 50, lambda: go_to_location("bedroom")),
        Button("Kitchen", 50, 250, 200, 50, lambda: go_to_location("kitchen")),
        Button("Go to City", 50, 350, 200, 50, lambda: go_to_location("city"))
    ]
    for button in buttons:
        button.draw(screen)
    return buttons

# Draw specific room screens
def draw_bathroom():
    screen.fill((135, 206, 250))  # Light sky blue background
    font = pygame.font.Font(None, 36)
    text_surface = font.render("You are in the Bathroom", True, (255, 255, 255))
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))

def draw_bedroom():
    screen.fill((123, 104, 238))  # Medium slate blue background
    font = pygame.font.Font(None, 36)
    text_surface = font.render("You are in the Bedroom", True, (255, 255, 255))
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))

def draw_kitchen():
    screen.fill((255, 228, 181))  # Moccasin background
    font = pygame.font.Font(None, 36)
    text_surface = font.render("You are in the Kitchen", True, (255, 255, 255))
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))

# Draw the city screen
def draw_city():
    screen.fill((240, 128, 128))  # Light coral background
    font = pygame.font.Font(None, 36)
    text_surface = font.render("You are in the City", True, (255, 255, 255))
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))

# Handle button click events
def handle_events(buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        for button in buttons:
            if button.is_clicked(event):
                button.callback()

    return True

# Change the current screen
def go_to_location(location):
    global current_screen
    print(f"Switching to {location}")  # Debug print statement
    current_screen = location


## THE GAME

# Main game loop
def main():
    global current_screen
    running = True
    current_screen = "home"

    while running:
        if current_screen == "home":
            buttons = draw_home_screen()
        else:
            buttons = []

        running = handle_events(buttons)

        if current_screen == "home":
            draw_home_screen()
        elif current_screen == "bathroom":
            draw_bathroom()
        elif current_screen == "bedroom":
            draw_bedroom()
        elif current_screen == "kitchen":
            draw_kitchen()
        elif current_screen == "city":
            draw_city()

        pygame.display.flip()

    pygame.quit()

# Entry point
if __name__ == "__main__":
    main()
