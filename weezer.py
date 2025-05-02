import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("weezer")
clock = pygame.time.Clock()
pygame.draw.line(screen, (0, 0, 0), (0, 0), (100, 100)) #wher is my line might fix later

# class of draggable images/ sprites 
class DraggableImage(pygame.sprite.Sprite):
    def __init__(self, image_path, pos):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (100, 100))  # Resize if needed
        self.rect = self.image.get_rect(topleft=pos)
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
# dragging function 
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and event.button == 1:
                self.dragging = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

# images 
image_files = ["brian bell.jpeg", "matt sharp.png", "pat wilson.jpeg", "rivers cuomo.jpeg"]
positions = [(50, 50), (100, 50), (150, 50), (200, 50)]

brian_bell = pygame.image.load("brian bell.jpeg") 
matt_sharp = pygame.image.load("matt sharp.png") 
pat_wilson = pygame.image.load("pat wilson.jpeg") 
rivers_cuomo = pygame.image.load("rivers cuomo.jpeg") 



# if position of the sprite is at a specific spot, trigger weezer 

brian_bell = (100, 500)
matt_sharp = (300, 500) 
pat_wilson = (500, 500)
rivers_cuomo = (700, 500)

target_positions = [(100, 500), (300, 500), (500, 500), (700, 500)]

# Create sprite group
pieces = [DraggableImage(img, pos) for img, pos in zip(image_files, positions)]
all_sprites = pygame.sprite.Group(pieces)

# Define positions for the 4 dots
dot_positions = [(100, 500), (300, 500), (500, 500), (700, 500)]  # Example positions
dot_radius = 5
dot_color = (255, 0, 0)  # Red color

# Define a function to check collision with tolerance
def is_colliding(sprite_pos, dot_pos, tolerance=10):
    return abs(sprite_pos[0] - dot_pos[0]) <= tolerance and abs(sprite_pos[1] - dot_pos[1]) <= tolerance

# Main loop
running = True
while running:
    screen.fill((24, 155, 204))  # Fill background

    # Draw 4 dots
    for pos in dot_positions:
        pygame.draw.circle(screen, dot_color, pos, dot_radius)

    # Update current positions of sprites
    current_positions = [piece.rect.center for piece in pieces]  # Use center for better collision detection

    # Check if all sprites are colliding with their respective dots
    rules = [is_colliding(current, target) for current, target in zip(current_positions, target_positions)]
    print("Rules:", rules)  # Debugging: Print rules

    if all(rules):
        print("omg its weezer!")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for piece in pieces:
            piece.handle_event(event)

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # 60 FPS setting

pygame.quit()
sys.exit()
