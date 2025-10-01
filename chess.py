import pygame
import chess

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (224, 184, 115)
DARK_BROWN = (139, 104, 69)

# Font for displaying text
font = pygame.font.SysFont("Arial", 32)

# Load images for the pieces
piece_images = {}
for piece in ['p', 'r', 'n', 'b', 'q', 'k']:
    piece_images[f'b{piece}'] = pygame.image.load(f'assets/b{piece}.png')
    piece_images[f'w{piece}'] = pygame.image.load(f'assets/w{piece}.png')

# Setup the chessboard
board = chess.Board()

# Helper function to draw the chessboard
def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board.piece_at(row * 8 + col)
            if piece:
                piece_name = piece.symbol()
                if piece_name.isupper():
                    piece_color = 'w'
                else:
                    piece_color = 'b'
                piece_image = piece_images[f'{piece_color}{piece_name.lower()}']
                screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def get_square_under_mouse():
    x, y = pygame.mouse.get_pos()
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row * 8 + col

# Main loop
selected_square = None
valid_moves = []
running = True
while running:
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            square = get_square_under_mouse()

            # Select a piece if not selected
            if selected_square is None:
                if board.piece_at(square):
                    selected_square = square
                    valid_moves = [move.to_square for move in board.legal_moves if move.from_square == selected_square]
            else:
                # Move the selected piece if it's a valid move
                if square in valid_moves:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                    selected_square = None
                    valid_moves = []

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = chess.Board()  # Reset the board
                selected_square = None
                valid_moves = []

    # Display valid moves
    for move in valid_moves:
        row, col = divmod(move, 8)
        pygame.draw.circle(screen, (0, 255, 0), (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

    # Display the board and pieces
    pygame.display.flip()

pygame.quit()
