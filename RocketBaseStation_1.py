import pygame

from Rocket import Rocket
import matplotlib
import random
import settings

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

    def __init__(self, label, color, chart_pos, data, ):
        self.x = chart_pos[0]
        self.y = chart_pos[1]
        self.label = label
        self.data = [[1], [1]]
        self.color = color
        fig = plt.figure(figsize=[3, 3])
        self.ax = fig.add_subplot(111)

        self.canvas = agg.FigureCanvasAgg(fig)

    def draw_plot(self):
        self.ax.plot(self.data[0], self.data[1], color= self.color)
        self.canvas.draw()
        renderer = self.canvas.get_renderer()

        raw_data = renderer.tostring_rgb()
        size = self.canvas.get_width_height()


        surface_to_return = pygame.Surface((size[0], size[1]))
        surface_to_return.blit(pygame.image.fromstring(raw_data, size, "RGB"), (0,0))
        font = pygame.font.SysFont('comicsans', 30)
        surface_to_return.blit(font.render(self.label, True, (0,0,0)),(0,0))
        return surface_to_return



# Our Draw function

def redrawWindow():
    win.fill((255, 255, 255))
    if not ourRocket.is_launched():
        launchButton.draw(win)
    else:

        timeButton.text = "AirTime: {:.2f}".format(ourRocket.getAirTime())
        timeButton.draw(win)


        win.blit(temperature_chart.draw_plot(), (temperature_chart.x, temperature_chart.y))

        win.blit(pressure_chart.draw_plot(), (pressure_chart.x, pressure_chart.y))

        win.blit(acceleration_chart.draw_plot(), (acceleration_chart.x, acceleration_chart.y))


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

    global temperature_chart, pressure_chart, acceleration_chart
    temperature_chart = DataPlot("temperature", 'red', (50,50) , [[1],[1]])

    pressure_chart = DataPlot("pressure", 'blue', (400,50), [[1], [1]])

    acceleration_chart = DataPlot("acceleration", 'green', (400, 400), [[1], [1]])

def main_loop():
    is_running = True
    is_mouse_over_button = False
    clock = pygame.time.Clock()
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
                temperature_chart.data = (ourRocket.timestamps, ourRocket.temps)
                pressure_chart.data = (ourRocket.timestamps, ourRocket.air_pressure)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__' :
    initialize()

    main_loop()
