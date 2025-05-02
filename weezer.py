import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("weezer")
clock = pygame.time.Clock()
pygame.draw.line(screen, (0, 0, 0), (0, 0), (100, 100))

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

#dot so i can position the sprites correctly
x = 400
y = 300
dot_radius = 5 
pygame.draw.circle(screen, (255, 0, 0), (x, y), dot_radius)
pygame.display.flip()

# if position of the sprite is at a specific spot, trigger weezer 

brian_bell = (50, 500)
matt_sharp = (200, 500) 
pat_wilson = (50, 500)
rivers_cuomo = (200, 500)

target_positions = [(50, 50), (100, 50), (150, 50), (200, 50)]
current_positions = [brian_bell, matt_sharp, pat_wilson, rivers_cuomo]

rules = [current == target for current, target in zip(current_positions, target_positions)]

if all(rules):
    print("omg its weezer!")

# Create sprite group
pieces = [DraggableImage(img, pos) for img, pos in zip(image_files, positions)]
all_sprites = pygame.sprite.Group(pieces)

# Main loop
running = True
while running:
    screen.fill((24, 155, 204))  # Fill background
    pygame.draw.circle(screen, (255, 0, 0), (x, y), dot_radius)  # Dot for positioning 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for piece in pieces:
            piece.handle_event(event)

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60) #60 FPS setting 

pygame.quit()
sys.exit()
