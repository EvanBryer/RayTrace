#!/usr/bin/python

import pygame
import math
# Standard resolution
screen = pygame.display.set_mode((1920, 1080))

running = True

# Lines to be drawn, blocks rays
lines = [
    [
        [1500, 200],
        [1200, 0]
    ],
    [
        [100, 200],
        [200, 500]
    ],
    [
        [700, 925],
        [950, 900]
    ]
]
# Calculate intersections between lines and rays
def intersect(start, x, y):
    X0 = start[0]
    X1 = x
    Y0 = start[1]
    Y1 = y
    for line in lines:
        X2 = line[0][0]
        X3 = line[1][0]
        Y2 = line[0][1]
        Y3 = line[1][1]

        s1_x = X1 - X0
        s1_y = Y1 - Y0
        s2_x = X3 - X2
        s2_y = Y3 - Y2
        s = (-s1_y * (X0 - X2) + s1_x * (Y0 - Y2)) / (-s2_x * s1_y + s1_x * s2_y)
        t = (s2_x * (Y0 - Y2) - s2_y * (X0 - X2)) / (-s2_x * s1_y + s1_x * s2_y)

        if s >= 0 and s <= 1 and t >= 0 and t <= 1:
            i_x = X0 + (t * s1_x)
            i_y = Y0 + (t * s1_y)
            return [i_x, i_y]
    return False

# Draw function, called every update
def draw():
    screen.fill([0, 100, 255])
    pos = pygame.mouse.get_pos()
    # Draw circle centered on cursor
    pygame.draw.circle(screen, [255, 255, 255], pos, 50)
    # Draw Lines
    for line in lines:
        pygame.draw.line(screen, [0, 0, 0], line[0], line[1], 10)
    # Throw Rays
    for start in range(0, 360, 6):
        end = start * math.pi / 180
        start *= math.pi / 180
        length = 999
        x = pos[0] + length * math.cos(end)
        y = pos[1] + length * math.sin(end)
        # Check if ray intersects with lines
        inter = intersect(pos, x, y)
        # If no intersection, draw as normal
        if not inter:
            pygame.draw.line(screen, [255, 255, 255], pos, [x, y], 5)
        # otherwise, color red and cut off at intersection point
        else :
            pygame.draw.line(screen, [255, 0, 0], pos, [inter[0], inter[1]], 5)
        # Draw to screen
    pygame.display.flip()

# Main loop
while running:
    draw()
    # Check for exit
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            running = False

print('Exited the main loop. Program will quit...')
quit() # Not actually necessary since the script will exit anyway.
