
Conversation opened. 2 messages. All messages read.

Skip to content
Using Acharya Institutes, Soldevanahalli, Bangalore Mail with screen readers
varalakshmi 

3 of many
Fwd: CGV program 1-6
Inbox

Varalakshmi B D <varalakshmi@acharya.ac.in>
Attachments
Tue, Jun 18, 2:39 PM
to 21.becs

Dear students 
PFA 1 to 6 CGIP lab programs

---------- Forwarded message ---------
From: Jawahar Jonathan K AI002393 <jawahar2393@acharya.ac.in>
Date: Tue, Jun 18, 2024, 14:35
Subject: CGV program 1-6
To: Varalakshmi B D <varalakshmi@acharya.ac.in>



Dear Mam
PFA

 6 Attachments
  •  Scanned by Gmail

MADESH P AIT21BECS004 <madeshp.21.becs@acharya.ac.in>
Attachments
Wed, Jun 19, 5:34 PM
to parrayhuzaif03


 6 Attachments
  •  Scanned by Gmail
varatanapalli. Press tab to insert.
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's Line Algorithm")

# Bresenham's line drawing algorithm
def draw_line_bresenham(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steep = dy > dx

    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    swapped = False
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
        swapped = True

    dx = x1 - x0
    dy = y1 - y0

    error = int(dx / 2.0)
    ystep = 1 if y0 < y1 else -1

    y = y0
    points = []
    for x in range(x0, x1 + 1):
        coord = (y, x) if steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    if swapped:
        points.reverse()

    return points

# Main loop
def main():
    start_point = (100, 100)
    end_point = (700, 400)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)

        # Draw the line using Bresenham's algorithm
        line_points = draw_line_bresenham(*start_point, *end_point)
        for point in line_points:
            pygame.draw.circle(screen, BLACK, point, 1)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
1.py
Displaying 1.py.