import time
from tkinter import *
from enum import Enum

class Colors(Enum):
    BLUE = 'blue'
    RED = 'red'
    GREEN = 'green'
    GREY = 'grey'
    YELLOW = 'yellow'


class PlaygroundWindow:

    def __init__(self, window_size):
        self.window_size = window_size

        self.master = Tk()
        self.master.title('Playground')
        self.master.protocol("WM_DELETE_WINDOW", lambda: self.master.destroy())
        self.master.bind('<Escape>', lambda e: self.master.destroy())

        self.canvas = Canvas(self.master, width=window_size[0], height=window_size[1], background='black')
        self.canvas.pack(fill=BOTH, expand=1)

    def put_oval_to_canvas(self, atom):
        pos_x, pos_y, rad, col = atom
        o = self.canvas.create_oval(pos_x - rad, pos_y - rad, pos_x + rad, pos_y + rad, fill=col)

        return o

    def update(self):
        self.master.update()

    def delete_item_from_canvas(self, item):
        self.canvas.delete(item)
    
    def get_window_size(self):
        return (self.canvas.winfo_width(), self.canvas.winfo_height())


def run(size, world):
    playground_window = PlaygroundWindow(size)
    playground_window.update()
    while True:
        winsize = playground_window.get_window_size()
        coords = world.tick(winsize[0], winsize[1])

        ovals = []
        for coord in coords:
            oval = playground_window.put_oval_to_canvas(coord)
            ovals.append(oval)

        playground_window.update()

        time.sleep(0.1)

        for oval in ovals:
            playground_window.delete_item_from_canvas(oval)
