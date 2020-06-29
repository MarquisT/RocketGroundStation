import pygame
from Rocket import Rocket
import matplotlib
import random

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg


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
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False

class DataPlot:

    def __init__(self, label, color, y_scale, starting_data):
        self.label = label
        self.data = starting_data
        self.color = color
        fig = plt.figure(figsize=[3, 3])
        self.ax = fig.add_subplot(111)

        self.canvas = agg.FigureCanvasAgg(fig)

    def draw_plot(self):
        self.ax.plot(self.data[0],self.data[1], color= self.color)
        self.canvas.draw()
        renderer = self.canvas.get_renderer()

        raw_data = renderer.tostring_rgb()
        size = self.canvas.get_width_height()

        return pygame.image.fromstring(raw_data, size, "RGB")

    def add_data(self,data_input_tuple):
        self.data[0].append(data_input_tuple[0])
        self.data[1].append(data_input_tuple[1])
# Our Draw function
def redrawWindow():
    win.fill((255, 255, 255))
    if not ourRocket.is_launched():
        launchButton.draw(win)
    else:

        timeButton.text = "AirTime: {:.2f}".format(ourRocket.getAirTime())
        timeButton.draw(win)

        tempChart = temperature_chart.draw_plot()
        win.blit(tempChart, (50, 50))




def quit_station():
    global is_running
    is_running = False
    pygame.quit()
    exit()


def initialize():


    pygame.init()
    global ourRocket
    ourRocket = Rocket()
    global win
    win = pygame.display.set_mode((1000, 700))

    pygame.display.set_caption("Rocket Base Station")

    global launchButton
    launchButton = Button((0, 255, 0), 50, 600, 250, 50, 'Launch!')

    global timeButton
    timeButton = Button((0, 255, 0), 50, 600, 300, 50, "Nothing yet")

    global temperature_chart
    temperature_chart = DataPlot("temperature", 'red', 0 , [[1,2,3,4],[5, 6, 7, 3]])


def main_loop():
    is_running = True
    is_mouse_over_button = False
    clock = pygame.time.Clock()
    cur_x = len(temperature_chart.data[1]) + 1
    while is_running:

        redrawWindow()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                quit_station()

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    temperature_chart.add_data((cur_x,random.randrange(0, 7)))
                    cur_x += 1
        if ourRocket.is_ready():
            if is_mouse_over_button:
                launchButton.color = (0, 100, 0)
            else:
                launchButton.color = (50, 255, 50)
        else:
            launchButton.color = (30, 30, 30)

        if ourRocket.is_launched():
            if ourRocket.is_changed():
                print(ourRocket.temps)

        pygame.display.flip()
        clock.tick(60)


initialize()

main_loop()
