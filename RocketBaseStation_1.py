import pygame
from Rocket import Rocket


# Class Declarations

class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                int(self.x + (self.width / 2 - text.get_width() / 2)),
                int(self.y + (self.height / 2 - text.get_height() / 2))))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False




# Let's initialize the required classes
ourRocket = Rocket()
pygame.init()
win = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Rocket Base Station")
is_running = True
clock = pygame.time.Clock()
is_mouse_over_button = False

#
launchButton = Button((0,255,0),50,600,250,50,'Launch!')

# Our Draw function
def redrawWindow():
    win.fill((255,255,255))
    launchButton.draw(win)




# Main Loop
while is_running:
    redrawWindow()
    pygame.display.flip()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ourRocket.is_ready():
                if launchButton.isOver(pos):
                    print('clicked the button')

        if event.type == pygame.MOUSEMOTION:
            if launchButton.isOver(pos):
                is_mouse_over_button = True

            else:
                is_mouse_over_button = False
    if ourRocket.is_ready():
        if is_mouse_over_button:
            launchButton.color = (0, 100, 0)
        else:
            launchButton.color = (50, 255, 50)
    else:
        launchButton.color = (30, 30, 30)
    clock.tick(60)