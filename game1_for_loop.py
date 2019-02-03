import sys, pygame
import time
import random
import math

class Ball:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.position = pygame.Rect(x, y, 75, 75)
        self.speed = speed
        self.size = 20
    def move(self):
        self.position = self.position.move(self.speed[0], self.speed[1])
        if self.position.x < 0 or self.position.x > width:
            self.speed[0] = -self.speed[0]
        if self.position.y < 0 or self.position.y > height:
            self.speed[1] = -self.speed[1]
    def move_down(self):
        self.position = self.position.move(0, 1)
    def move_up(self):
        self.position = self.position.move(0, -1)
    def move_right(self):
        self.position = self.position.move(1, 0)
    def move_left(self):
        self.position = self.position.move(-1, 0)

pygame.init()
pygame.key.set_repeat(1, 1)
balls = [] #List of objects of Ball class
size = width, height = 800, 600
map_tiles = []
map_rows = 30
map_cols = 40
currentY = 0
currentX = 0
speed = [2, 2]
black = 0,0,0
white = 255,255,255
t1 = 0
t2 = 0
counter = 0
delta_list = [] # list of frame times
delta_sum = 0 # sum of frametimes
delta_sum_counter = 0 #number of frames with counted times of execution

# Generating Mapdddd
map_tiles = [[random.randint(0,2) for col in range(map_cols)] for row in range(map_rows)]
print(map_tiles)

screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 20)
frame_time_text = font.render("Frame time:", False, white)
ball = pygame.image.load("img/ball2_75_8bit.png").convert_alpha()
background = pygame.image.load("img/old-map-vintage-texture.gif").convert()
tile1 = pygame.image.load("img/travka.png").convert()
tile2 = pygame.image.load("img/tile2.png").convert()
screen.blit(background, (0, 0))
for i in range (0,2):
    balls.append(Ball(random.randint(0, width-100), random.randint(0, height-100), [random.randint(-2, 2), random.randint(-2,2)]))
    
t_start = time.time()

while 1:
    counter += 1
    t1 = time.time()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        if currentY < 2300:
            currentY += 1
    if keys[pygame.K_a]:
        if currentX > 0:
            currentX -= 1
    if keys[pygame.K_w]:
        if currentY > 0:
            currentY -= 1
    if keys[pygame.K_d]:
        if currentX < 3100:
            currentX += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    if counter < 0:
        print(delta_sum_counter)
        print("Average Frame Time:")
        print(delta_sum/delta_sum_counter)
        time_total = time.time() - t_start
        print("Total execution time:")
        print(time_total)
        pygame.quit()
        sys.exit()

    for row in range(6):
        for col in range(8):
            if map_tiles[row+math.floor(currentY/100)][col+math.floor(currentX/100)] == 1:
                screen.blit(tile1, (col * 100, row * 100))
            else:
                screen.blit(tile2, (col * 100, row * 100))

    #screen.blit(background, (0, 0))
    #screen.fill(black)
    #for element in balls:
    #    screen.blit(background, element.position, element.position)
    #for element in balls:
        #element.move()
        #screen.blit(ball, element.position)
    
    frame_time = pygame.time.Clock().tick()
    my_text = "Current X: {} Current Y: {}".format(currentX, currentY)
    text = font.render(str(my_text), False, white)
    screen.blit(text, (10, 10))
    screen.blit(frame_time_text, (10, 30))
    pygame.display.flip()

    # Measuring Time
    delta = round(((time.time() - t1)*1000),2)
    delta_sum_counter += 1
    delta_sum += delta
    if delta_sum_counter == 100:
        average_frame_time = round(delta_sum/delta_sum_counter,3)
        delta_sum_counter = 0
        delta_sum = 0
        frame_time_text = font.render("Frame time: {}".format(average_frame_time), False, white)
        #delta_list.append(delta)
        #print(delta)



    
    
    

