import pygame

pygame.init()


class Rocket:

    def __init__(self):
        self.is_ready = False

    def is_ready(self):
        return self.is_ready

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


def redrawWindow():
    win.fill((255, 255, 255))
    greenButton.draw(win)


win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('rocket base station')

x = 50
y = 50
width = 40
height = 60
vel = 5
clock = pygame.time.Clock()

greenButton = Button((0, 255, 0), 150, 225, 250, 100, 'Text')
is_running = True

while is_running:
    redrawWindow()
    pygame.display.flip()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton.isOver(pos):
                print('clicked the button')
        if event.type == pygame.MOUSEMOTION:
            if greenButton.isOver(pos):
                greenButton.color = (0, 100, 0)
            else:
                greenButton.color = (50, 255, 50)

    clock.tick(60)
