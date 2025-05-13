# sort using cocktail sort!
# last modified: 03/14/2024

import pygame
import random
import sys

pygame.init()

# initialize window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BAR_HEIGHT_MAX = 400
FPS = 60

# colors!!!
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cocktail Shaker Sort Visualizer")

clock = pygame.time.Clock()

# Font for text
font = pygame.font.SysFont("arial", 30)

def generate_bars():
    # randomly generate 25 - 100 bars
    num_bars = random.randint(25, 100)
    return [{'height': random.randint(50, BAR_HEIGHT_MAX), 'color': WHITE} for _ in range(num_bars)]

bars = generate_bars()

def cocktail_shaker_sort_step(bars, start, end, index, direction):
    swapped = False

    for bar in bars:
        bar['color'] = WHITE

    i = index
    if direction == 1 and i < end:
        if bars[i]['height'] > bars[i + 1]['height']:
            bars[i], bars[i + 1] = bars[i + 1], bars[i]
            swapped = True
        bars[i]['color'] = GREEN
        bars[i + 1]['color'] = GREEN
        index += 1
    elif direction == -1 and i > start:
        if bars[i - 1]['height'] > bars[i]['height']:
            bars[i - 1], bars[i] = bars[i], bars[i - 1]
            swapped = True
        bars[i - 1]['color'] = GREEN
        bars[i]['color'] = GREEN
        index -= 1

    if direction == 1 and index >= end:
        index = end
        direction = -1
        end -= 1
    elif direction == -1 and index <= start:
        index = start
        direction = 1
        start += 1

    return start, end, index, direction, swapped

running = True
start = 0
end = len(bars) - 1
index = 0
direction = 1
sorted = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r and sorted:
            bars = generate_bars()
            start = 0
            end = len(bars) - 1
            index = 0
            direction = 1
            sorted = False

    if not sorted and start <= end:
        start, end, index, direction, swapped = cocktail_shaker_sort_step(bars, start, end, index, direction)
        if start > end:
            sorted = True
            for bar in bars:
                bar['color'] = WHITE

    screen.fill(BLACK)
    bar_width = SCREEN_WIDTH // len(bars)
    for i, bar in enumerate(bars):
        x = i * bar_width
        y = SCREEN_HEIGHT - bar['height']
        pygame.draw.rect(screen, bar['color'], (x, y, bar_width, bar['height']))

    if not sorted:
        pygame.draw.line(screen, RED, (index * bar_width, 0), (index * bar_width, SCREEN_HEIGHT), 2)

    if sorted:
        text = font.render("Press the R key to sort a random design again!", True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(FPS)
    pygame.time.delay(10)

pygame.quit()
sys.exit()