import pygame
from random import randint

class Fruit:
    def __init__(self, screen, color, size):
        self.color = color
        self.screen = screen
        self.pos_x = randint(0,screen.get_width()/size)*size
        self.pos_y = randint(0,screen.get_height()/size)*size
        self.size = size
        self.pixel = pygame.Rect(self.pos_x,self.pos_y,self.size,self.size)
    
    def draw(self):
        pygame.draw.rect(self.screen,self.color, self.pixel)

    def new(self):
        self.pos_y = randint(0,(screen.get_height()/self.size)-1)*self.size
        self.pos_x = randint(0,(screen.get_width()/self.size)-1)*self.size
        self.pixel = pygame.Rect(self.pos_x,self.pos_y,self.size,self.size)

class Snake:
    def __init__(self, screen, color, size):
        self.color = color
        self.screen = screen
        self.pos_x = int(screen.get_width()/size)*size/2 
        self.pos_y = int(screen.get_height()/size)*size/2 
        self.direction = (0,0)
        self.size = size
        self.snake_body = pygame.Rect(self.pos_x,self.pos_y,self.size,self.size)
        self.snake = [self.snake_body]

    def draw(self):
        for loop_snake_body in self.snake: 
            pygame.draw.rect(self.screen, self.color, loop_snake_body)

    def move(self, direction):
        t_snake_body = self.snake[0].copy()
        t_snake_body.move_ip(direction)
        self.snake.insert(0,t_snake_body)
        self.snake.pop()
    
    def move_add(self, direction):
        t_snake_body = self.snake[0].copy()
        t_snake_body.move_ip(direction)
        self.snake.insert(0,t_snake_body)

if __name__ == "__main__":
    # initial conditions and Flags
    pixel_size = 20
    speed = 10
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    fruit = Fruit(screen, "red",pixel_size)
    snake = Snake(screen, "blue",pixel_size)
    running = True
    direction = (0,0)                               # Starting direction (0,0)
    score = 10

    # Enter Player Name 
    player = input("Enter Player Name: ")

    # Main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")

        # Begin gameplay
        
        # Draw snake and fruit
        # pygame.draw.rect(screen,"red", pygame.Rect(10,10,50,50))
        fruit.draw()
        snake.draw()

        # read in keys and set direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]: 
            running = False
        if keys[pygame.K_DOWN]:
            direction = (0,1*pixel_size)
        if keys[pygame.K_UP]:
            direction = (0,-1*pixel_size)
        if keys[pygame.K_LEFT]:
            direction = (-1*pixel_size,0)
        if keys[pygame.K_RIGHT]:
            direction = (1*pixel_size,0)

        # Fruit collision detection
        if snake.snake[0].center == fruit.pixel.center:
            fruit.new()
            snake.move_add(direction)
            speed += 3
            score += 10
        elif (snake.snake[0].centerx < 0) or (snake.snake[0].centerx > screen.get_width()):
            running = False
        elif (snake.snake[0].centery < 0) or (snake.snake[0].centery > screen.get_height()):
            running = False
        else:
            snake.move(direction)
        
        pygame.display.flip()

        clock.tick(speed) / 1000

    print(f"Score = {score}")


    pygame.quit()
