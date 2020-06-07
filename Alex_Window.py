import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Rocket Base Station')

run = True
xfirst = 100
yfirst = 400
widthfirst = 350
heightfirst = 50
vel = 5

def redrawWindow():
    win.fill((255,255,255))
    launchbutton.draw(win)


class button():
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
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


launchbutton = button((0,255,0),xfirst,yfirst,widthfirst,heightfirst,'Launch Rocket')
while run:
    redrawWindow()
    pygame.display.flip()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if launchbutton.isOver(pos):
                print("Rocket Launched!")
        if launchbutton.isOver(pos):
            launchbutton.color = (255,255,0)
        else:
            launchbutton.color = (0, 255, 0)
    pygame.display.update()


pygame.quit()