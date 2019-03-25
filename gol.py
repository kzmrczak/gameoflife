import numpy,random, pygame, time


def makeBoard(x,y):
    array = numpy.zeros((x,y))
    for i in range(x):
        for j in range(y):
            r = random.randint(0,1)
            array[i][j] = r
    return array




cols = 100
rows = 100
grid = makeBoard(cols,rows)
next = makeBoard(cols, rows)


def countNeighbors(board, x, y):
    global cols, rows
    sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            row = (y + i + rows) % rows
            col = (x + j + cols) % cols

            sum += grid[row][col]
    sum -= grid[x][y]
    return sum


HEIGHT = 3
WIDTH = 3
MARGIN = 1

bg = (0,0,0)
ones = (255, 255, 255)
zeros = (0,0,0)

pygame.init()
WINDOW_SIZE = [cols*(HEIGHT+MARGIN), rows*(WIDTH+MARGIN)]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
done = True

while done:
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False


    for row in range(rows):
            for column in range(cols):
                color = zeros
                if grid[row][column] == 1:
                    color = ones
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])


    # oblicz nast bazujac na poprzedniej
    for i in range(rows):
        for j in range(cols):
            state = grid[i][j]
            neighbors = countNeighbors(grid, i, j)
            if state == 0 and neighbors == 3:
                next[i][j] = 1
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                next[i][j] = 0
            else:
                next[i][j] = state


    grid = next
    #time.sleep(0.09)
    pygame.display.flip()

	# to jest test
pygame.quit()