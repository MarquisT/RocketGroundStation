import pygame
from Rocket import Rocket
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

fig = plt.figure(figsize=[3, 3])
ax = fig.add_subplot(111)
canvas = agg.FigureCanvasAgg(fig)






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
timeButton =  Button((0, 255, 0), 50, 600, 300, 50, "Nothing yet")


data = [5, 6, 7, 3]



# Our Draw function
def redrawWindow():
    win.fill((255,255,255))
    if not ourRocket.is_launched():
        launchButton.draw(win)
    else:
        timeButton.text = "AirTime: {:.2f}".format(ourRocket.getAirTime())
        timeButton.draw(win)




# Graph Function
def plot(data):
   ax.plot(data)
   canvas.draw()
   renderer = canvas.get_renderer()

   raw_data = renderer.tostring_rgb()
   size = canvas.get_width_height()

   return pygame.image.fromstring(raw_data, size, "RGB")


# Main Loop
while is_running:

    redrawWindow()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ourRocket.is_ready() and not ourRocket.is_launched():
                if launchButton.isOver(pos):
                    print('clicked the button')
                    ourRocket.launch()

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


    if ourRocket.is_launched():
        tempChart = plot(data)
        win.blit(tempChart, (50, 50))




    pygame.display.flip()
    clock.tick(60)