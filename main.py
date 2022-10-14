from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

root.configure(bg = "black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False,False)

top_frame = Frame(
    root,
    bg = 'black',
    width = settings.WIDTH,
    height = utils.height_percent(15)
)
top_frame.place(x=0, y=0)


left_frame = Frame(
    root,
    bg = 'black',
    width = utils.width_percent(25),
    height = utils.height_percent(85)
)
left_frame.place(x=0, y=utils.height_percent(15))


center_frame = Frame(
    root,
    bg = 'black',
    width = utils.width_percent(75),
    height = utils.height_percent(85)
)
center_frame.place(x= utils.width_percent(25), y=utils.height_percent(15))

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)


game_title.place(
    x=utils.width_percent(25), y=0
)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(x=10, y= 50)


for x in range(settings.GRID):
    for y in range(settings.GRID):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column = y, row = x)


Cell.randomized_mines()

for i in Cell.all:
    print(i.is_mine)

root.mainloop()