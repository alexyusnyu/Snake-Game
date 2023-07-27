import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (0, 0, 0)


class Skull:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/skull.png").convert()
        self.image2 = pygame.image.load("resources/skullbody.png").convert()
        self.length = 1
        self.x = [760]
        self.y = [120]
        self.direction = 'left'

    def draw(self):
        if self.length <= 1:
            for i in range(self.length):
                self.parent_screen.blit(self.image, (self.x[0], self.y[0]))

        if self.length > 1:
            for i in range(self.length):
                self.parent_screen.blit(self.image, (self.x[0], self.y[0]))
                self.parent_screen.blit(self.image2, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move(self):
        for i in range(self.length):
            self.y[i] = random.randint(1, 19) * SIZE
            self.x[i] = 920

    def walk(self):
        # update body
        if self.length <= 1:
            for i in range(self.length - 1, 0, -1):
                self.x[0] = self.x[i - 1]
                self.y[0] = self.y[i - 1]

        if self.length > 1:
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE / 2
        if self.direction == 'right':
            self.x[0] += SIZE / 2
        if self.direction == 'up':
            self.y[0] -= SIZE / 2
        if self.direction == 'down':
            self.y[0] += SIZE / 2

        self.draw()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def decrease_length(self):
        self.length -= 1
        self.x.append(-1)
        self.y.append(-1)


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.length = 1
        self.x = 40
        self.y = 320
        self.direction = 'right'

    def draw(self):

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y = random.randint(1, 19) * SIZE
        self.x = 40

    def walk(self):
        # update body
        for i in range(self.length - 1, 0, -1):
            self.x = self.x[i - 1]
            self.y = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x -= SIZE / 4
        if self.direction == 'right':
            self.x += SIZE / 4
        if self.direction == 'up':
            self.y -= SIZE / 4
        if self.direction == 'down':
            self.y += SIZE / 4

        self.draw()


class Apple2:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.length = 1
        self.x = 40
        self.y = 720
        self.direction = 'up'

    def draw(self):

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y = 720
        self.x = random.randint(1, 24) * SIZE

    def walk(self):
        # update body
        for i in range(self.length - 1, 0, -1):
            self.x = self.x[i - 1]
            self.y = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x -= SIZE / 4
        if self.direction == 'right':
            self.x += SIZE / 4
        if self.direction == 'up':
            self.y -= SIZE / 4
        if self.direction == 'down':
            self.y += SIZE / 4

        self.draw()


class Bird:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/bird.jpg").convert()
        self.length = 1
        self.x = 440
        self.y = 40
        self.direction = 'down'

    def draw(self):

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = 40

    def walk(self):
        # update body
        for i in range(self.length - 1, 0, -1):
            self.x = self.x[i - 1]
            self.y = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x -= SIZE / 4
        if self.direction == 'right':
            self.x += SIZE / 4
        if self.direction == 'up':
            self.y -= SIZE / 4
        if self.direction == 'down':
            self.y += SIZE / 4

        self.draw()


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/snakehead.jpg").convert()
        self.image2 = pygame.image.load("resources/snakebody.jpg").convert()
        self.direction = 'right'

        self.length = 1
        self.x = [400]
        self.y = [720]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOR)
        if self.length <= 1:
            for i in range(self.length):
                self.parent_screen.blit(self.image, (self.x[0], self.y[0]))

        if self.length > 1:
            for i in range(self.length):
                self.parent_screen.blit(self.image, (self.x[0], self.y[0]))
                self.parent_screen.blit(self.image2, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def decrease_length(self):
        self.length -= 1
        self.x.append(-1)
        self.y.append(-1)


def is_collision(x1, y1, x2, y2):
    if x2 <= x1 < x2 + SIZE:
        if y2 <= y1 < y2 + SIZE:
            return True
    return False


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake And Apple Game")
        self.surface = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.apple2 = Apple2(self.surface)
        self.bird = Bird(self.surface)
        self.skull = Skull(self.surface)

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.apple2 = Apple2(self.surface)
        self.bird = Bird(self.surface)
        self.skull = Skull(self.surface)

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.walk()
        self.apple2.walk()
        self.bird.walk()
        self.skull.walk()
        self.display_score()
        pygame.display.flip()

        if self.snake.is_collision_with_apple(self.apple):
            self.snake.increase_length()
            self.apple.move()

        if self.snake.is_collision_with_apple2(self.apple2):
            self.snake.increase_length()
            self.apple2.move()

        if self.snake.is_collision_with_skull(self.skull):
            self.snake.decrease_length()

        if self.snake.is_collision_with_bird(self.bird):
            self.snake.increase_length()
            self.bird.move()

        if self.snake.length == 0:
            raise Exception("You are dead!")

        if not (0 <= self.snake.x[0] < 1000 and 0 <= self.snake.y[0] < 800):
            raise Exception("Hit the boundary error")

        if not (0 <= self.bird.x < 1000 and 0 <= self.bird.y < 800):
            self.bird.move()

        if not (0 <= self.apple.x < 1000 and 0 <= self.apple.y < 800):
            self.apple.move()

        if not (0 <= self.apple2.x < 1000 and 0 <= self.apple2.y < 800):
            self.apple2.move()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False
                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            self.clock.tick(10)  # Set the game's frame rate

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()