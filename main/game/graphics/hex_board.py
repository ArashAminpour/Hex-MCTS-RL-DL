import pygame

# Initialize Pygame and create a window to display the board
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)

# Create a 2D array to represent the cells of the board
board = [[0 for x in range(11)] for y in range(11)]

# Main loop to handle events and draw the board
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the hexagons to represent the cells of the board
    for i in range(11):
        for j in range(11):
            if board[i][j] == 0:
                pygame.draw.polygon(screen, (255, 255, 255), [(i*50, j*50), (i*50+25, j*50-25), (i*50+50, j*50), (i*50+25, j*50+25), (i*50, j*50)], 0)
            elif board[i][j] == 1:
                pygame.draw.polygon(screen, (255, 0, 0), [(i*50, j*50), (i*50+25, j*50-25), (i*50+50, j*50), (i*50+25, j*50+25), (i*50, j*50)], 0)
            elif board[i][j] == 2:
                pygame.draw.polygon(screen, (0, 0, 255), [(i*50, j*50), (i*50+25, j*50-25), (i*50+50, j*50), (i*50+25, j*50+25), (i*50, j*50)], 0)

    # Update the display
    pygame.display.flip()
