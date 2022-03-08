from queue import PriorityQueue
import pygame
import sys

import row

UNVISITED_COLOR = (122, 161, 210)  # light blue
VISITED_COLOR = (120, 255, 214)  # light green
GOAL_COLOR = (100, 145, 115)  # dark green
BLOCK_COLOR = (255, 255, 255)  # white
WALL_COLOR = (12, 53, 71)  # dark blue
PATH_COLOR = (233, 211, 98)  # yellow
GRID_COLOR = (67, 67, 67)  # dark grey
SOURCE_COLOR = (100, 145, 115)  # dark green

grid = []  # 2D array of cells
path = []  # list of cells


class block:  # block class
    def __init__(self, i, j):  # constructor
        self.x = i  # x coordinate
        self.y = j  # y coordinate
        self.source = False  # is source
        self.wall = False  # is wall
        self.goal = False  # is goal
        self.queue = False  # is in queue or stack
        self.visited = False  # is visited
        self.neighbours = []  # list of neighbours
        self.prior = None  # priority
        self.level = 0  # level of cell

    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * block_width, self.y * block_height, block_width, block_height))

    def set_neighbours(self):
        if self.y > 0:  # if not on top row
            self.neighbours.append(grid[self.x][self.y - 1])  # add top neighbour
        if self.x < columns - 1:  # if not on right column
            self.neighbours.append(grid[self.x + 1][self.y])  # add right neighbour
        if self.y < rows - 1:  # if not on bottom row
            self.neighbours.append(grid[self.x][self.y + 1])  # add bottom neighbour
        if self.x > 0:  # if not on left column
            self.neighbours.append(grid[self.x - 1][self.y])  # add left neighbour

    def __lt__(self, other):
        return False


def bresenham(p0, p1):  # Bresenham's line algorithm concatenates 2 points of a line
    x0, y0 = p0  # start point
    x1, y1 = p1  # end point
    dx = abs(x1 - x0)  # delta x
    dy = abs(y1 - y0)  # delta y
    x, y = x0, y0  # current point
    sx = -1 if x0 > x1 else 1  # step x
    sy = -1 if y0 > y1 else 1  # step y
    if dx > dy:  # slope < 1
        err = dx / 2.0
        while x != x1:
            grid[x][y].wall = True  # set wall
            err -= dy  # reduce
            if err < 0:
                y += sy  # step y
                err += dx  # reduce
            x += sx  # step x
    else:
        err = dy / 2.0
        while y != y1:
            grid[x][y].wall = True  # set wall
            err -= dx  # reduce
            if err < 0:
                x += sx  # step x
                err += dy  # reduce
            y += sy  # step y
    grid[x][y].wall = True  # set wall


f = open("input.txt", "r")  # open file
columns, rows = [int(x) for x in f.readline().split()]  # read rows and columns

for i in range(columns):  # create grid
    grid.append([])  # add row
    for j in range(rows):  # add column
        grid[i].append(block(i, j))  # add block

for i in range(columns):
    for j in range(rows):
        grid[i][j].set_neighbours()

poly = []  # list of points
polyList = []  # list of polygons

source_x, source_y, goal_x, goal_y = [int(x) for x in f.readline().split()]  # read source and goal coordinates

polyCount = eval(f.readline())  # read number of polygons

for i in range(polyCount):
    poly = f.readline()  # read polygon
    poly = [int(x) for x in poly.split()]  # convert to list
    temp = []  # temporary list
    for j in range(0, int(len(poly) / 2)):  # convert to 2D list
        temp.append((poly[j * 2], poly[j * 2 + 1]))  # add point
    polyList = temp  # add to list
    for j in range(0, len(polyList)):
        if (j == len(polyList) - 1):  # if last point
            bresenham(polyList[j], polyList[0])  # draw line
        else:
            bresenham(polyList[j], polyList[j + 1])  # draw line

f.close()  # close file

source_block = grid[source_x][source_y]  # source block
source_block.source = True  # set source
goal_block = grid[goal_x][goal_y]  # goal block
goal_block.goal = True  # set goal

algorithm = int(input(
    "Enter algorithm:\n1. Breadth-first search\n2. Uniform-cost Search\n3. Iterative deepening search\n4. Greedy-best first search\n5. A*\n"))

block_width = 30
block_height = 30

window_width = columns * block_width
window_height = rows * block_height

window = pygame.display.set_mode((window_width, window_height))  # create window


def draw_grid(win):
    for j in range(columns):
        pygame.draw.line(win, GRID_COLOR, (j * block_width, 0), (j * block_width, window_height))
        for i in range(rows):
            pygame.draw.line(win, GRID_COLOR, (0, i * block_height), (window_width, i * block_height))


def draw():  # draw grid and blocks
    window.fill(BLOCK_COLOR)  # fill window with color
    for i in range(columns):
        for j in range(rows):
            block = grid[i][j]  # current block
            block.draw(window, BLOCK_COLOR)  # draw block
            if block.queue:  # if in queue
                block.draw(window, UNVISITED_COLOR)  # draw block
            if block.visited:  # if visited
                block.draw(window, VISITED_COLOR)  # draw block
            if block in path:  # if in path
                block.draw(window, PATH_COLOR)  # draw block
            if block.source:  # if source
                block.draw(window, SOURCE_COLOR)  # draw block
            if block.wall:  # if wall
                block.draw(window, WALL_COLOR)  # draw block
            if block.goal:  # if goal
                block.draw(window, GOAL_COLOR)  # draw block
    draw_grid(window)  # draw grid
    window.blit(pygame.transform.flip(window, False, True), (0, 0))  # reverse window upside down
    pygame.display.flip()  # update window


def h(p1, p2):  # heuristic function
    x1, y1 = p1  # start point
    x2, y2 = p2  # end point
    return abs(x1 - x2) + abs(y1 - y2)  # manhattan distance


def BFS(source_block, goal_block):  # breadth-first search
    cost = 0
    queue = []
    queue.append(source_block)  # add source to queue
    source_block.visited = True  # set visited
    while len(queue) > 0:
        current_block = queue.pop(0)  # remove first element from queue
        current_block.visited = True  # set visited
        if current_block == goal_block:  # if found goal
            while current_block.prior != source_block:  # while not at source
                path.append(current_block.prior)  # add to path
                current_block = current_block.prior  # go to prior
                current_block.path = True  # set path
                cost += 1  # increment cost
            print("Cost: " + str(cost))  # print cost
            return
        else:
            for neighbour in current_block.neighbours:
                if not neighbour.queue and not neighbour.wall:  # if not in queue and not wall
                    neighbour.prior = current_block  # set prior
                    neighbour.queue = True  # set queue
                    queue.append(neighbour)  # add to queue
        draw()  # draw
    print("Path not found")  # print path not found


def AStar(source_block, goal_block):  # A*
    cost = 0
    count = 0
    pq = PriorityQueue()
    pq.put((0, count, source_block))  # add source to queue
    source_block.visited = True  # set visited
    g = {block: float("inf") for row in grid for block in row}  # set g to infinity
    g[source_block] = 0  # set g of source to 0
    f = {block: float("inf") for row in grid for block in row}  # set f to infinity
    f[source_block] = h((source_block.x, source_block.y), (goal_block.x, goal_block.y))  # set f of source to h

    while not pq.empty():  # while queue not empty
        current_block = pq.get()[2]  # get current block
        current_block.visited = True  # set visited
        if current_block == goal_block:  # if found goal
            while current_block.prior != source_block:  # while not at source
                path.append(current_block.prior)  # add to path
                current_block = current_block.prior  # go to prior
                current_block.path = True  # set path
                cost += 1  # increment cost
            print("Cost: " + str(cost))  # print cost
            return
        else:
            for neighbour in current_block.neighbours:
                if not neighbour.queue and not neighbour.wall:  # if not in queue and not wall
                    neighbour.prior = current_block  # set prior
                    neighbour.queue = True  # set queue
                    g[neighbour] = g[current_block] + 1  # set g of neighbour to g of current block + 1
                    f[neighbour] = g[neighbour] + h((neighbour.x, neighbour.y), (
                        goal_block.x, goal_block.y))  # set f of neighbour to g of neighbour + h
                    pq.put((f[neighbour], count, neighbour))  # add to queue
                    count += 1  # increment count
        draw()  # draw
    print("Path not found")


def IDDFS(source_block, goal_block, max_depth):  # iterative deepening search
    cost = 0
    stack = []
    stack.append(source_block)  # add source to stack
    source_block.visited = True  # set visited
    while len(stack) > 0:  # while stack not empty
        current_block = stack.pop()  # remove last element from stack
        current_block.visited = True  # set visited
        if current_block == goal_block:  # if found goal
            while current_block.prior != source_block:  # while not at source
                path.append(current_block.prior)  # add to path
                current_block = current_block.prior  # go to prior
                current_block.path = True  # set path
                cost += 1  # increment cost
            print("Cost: " + str(cost))  # print cost
            return
        else:
            if current_block.level > max_depth:  # if current block level is greater than max depth
                continue  # continue
            for neighbour in current_block.neighbours:
                if not neighbour.visited and not neighbour.wall:  # if not in queue and not wall
                    neighbour.prior = current_block  # set prior
                    neighbour.queue = True  # set queue
                    neighbour.level = current_block.level + 1  # set level
                    stack.append(neighbour)  # add to stack
        draw()  # draw
    print("Path not found")


def UCS(source_block, goal_block):  # uniform cost search
    cost = 0
    count = 0
    pq = PriorityQueue()  # priority queue
    pq.put((0, count, source_block))  # add source to queue
    source_block.visited = True  # set visited
    g = {block: float("inf") for row in grid for block in row}  # set g to infinity
    g[source_block] = 0  # set g of source to 0

    while not pq.empty():  # while queue not empty
        current_block = pq.get()[2]  # get current block
        current_block.visited = True  # set visited
        if current_block == goal_block:  # if found goal
            while current_block.prior != source_block:  # while not at source
                path.append(current_block.prior)  # add to path
                current_block = current_block.prior  # go to prior
                current_block.path = True  # set path
                cost += 1  # increment cost
            print("Cost: " + str(cost))  # print cost
            return
        else:
            for neighbour in current_block.neighbours:
                if not neighbour.queue and not neighbour.wall:  # if not in queue and not wall
                    neighbour.prior = current_block  # set prior
                    neighbour.queue = True  # set queue
                    g[neighbour] = g[current_block] + 1  # set g of neighbour to g of current block + 1
                    pq.put((g[neighbour], count, neighbour))  # add to queue
                    count += 1  # increment count
        draw()  # draw
    print("Path not found")


def Greedy(source_block, goal_block):
    cost = 0
    count = 0
    pq = PriorityQueue()
    pq.put((0, count, source_block))  # add source to queue
    source_block.visited = True  # set visited
    f = {block: float("inf") for row in grid for block in row}  # set f to infinity
    f[source_block] = h((source_block.x, source_block.y),
                        (goal_block.x, goal_block.y))  # set f of source to h of source
    while not pq.empty():  # while queue not empty
        current_block = pq.get()[2]  # get current block
        current_block.visited = True  # set visited
        if current_block == goal_block:  # if found goal
            while current_block.prior != source_block:  # while not at source
                path.append(current_block.prior)  # add to path
                current_block = current_block.prior  # go to prior
                current_block.path = True  # set path
                cost += 1  # increment cost
            print("Cost: " + str(cost))  # print cost
            return
        else:
            for neighbour in current_block.neighbours:
                if not neighbour.queue and not neighbour.wall:  # if not in queue and not wall
                    neighbour.prior = current_block  # set prior
                    neighbour.queue = True  # set queue
                    f[neighbour] = h((neighbour.x, neighbour.y),
                                     (goal_block.x, goal_block.y))  # set f of neighbour to h of neighbour
                    pq.put((f[neighbour], count, neighbour))  # add to queue
                    count += 1  # increment count
        draw()  # draw
    print("Path not found")


def main():
    begin_search = True
    while True:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if begin_search:
            if algorithm == 1:
                BFS(source_block, goal_block)
                begin_search = False
            elif algorithm == 2:
                UCS(source_block, goal_block)
                begin_search = False
            elif algorithm == 3:
                IDDFS(source_block, goal_block, 45)
                begin_search = False
            elif algorithm == 4:
                Greedy(source_block, goal_block)
                begin_search = False
            elif algorithm == 5:
                AStar(source_block, goal_block)
                begin_search = False


main()
