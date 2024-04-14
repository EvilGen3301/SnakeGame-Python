import tkinter 
import random
from turtle import window_height, window_width

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOWS_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
# Window game
window = tkinter.Tk()
window.title('snake')
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOWS_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

# Code here for game to be in center

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

# Game
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)    # Snakes head 
food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)
snake_body = [] # Snake body
velocityX = 0
velocityY = 0
score = 0

def change_direction(e):
    print(e.keysym)
    global velocityX, velocityY
    
    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0
        
def move():
    global snake, food, snake_body, score
    
    # Collision
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE
        score += 1
    
    # Update snake body
    for i in range(len(snake_body) - 1, -1, -1):
        tile = snake_body[i]
        if(i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y
        
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE
    
    

def draw():
    global snake, food, snake_body, score
    move()
    
    canvas.delete('all')

    # food draw
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = 'red')
    
    # snake draw
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = 'green')   
    
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = 'green')


    if True:
        canvas.create_text(WINDOW_WIDTH / 1.1, WINDOWS_HEIGHT / 1.1, font = 'Arial', text = f'score: {score}', fill = 'white')
    # If u want to change difficulty of the game use more ms like 150 or 200
    window.after(100, draw) # Loop for draw every 100 ms / 10 fps
    
    
draw()

window.bind('<KeyRelease>', change_direction)
window.mainloop()

