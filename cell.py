from tkinter import Button, Label
import random
import ctypes
import sys
import settings


class Cell:
    all = []
    cell_count_label = None
    cell_count = settings.CELL_COUNT

    def __init__(self, x, y,is_mine = False):
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.cell_btn_object = None
        self.is_opened = False
        self.is_mine_candidate = False

        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            height= 4, width=10,
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)

        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label = lbl

    def left_click_action(self, event):
        if self.is_mine == True:
            self.pressed_mine()


        else:
            if self.number_of_surrounding_mines ==0:
                for cell_obj in self.surrounding_mines:
                    cell_obj.show_mine()

            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game Over', 0)

                # Cancel Left and Right click events if cell is already opened:
            self.cell_btn_object.unbind('<Button-1>')
            self.cell_btn_object.unbind('<Button-3>')

            self.show_mine()

    def show_mine(self):
        if self.is_opened == False:
            Cell.cell_count -=1
            if Cell.cell_count_label:
                Cell.cell_count_label.configure(text= f"Cells left: {Cell.cell_count}")

        self.cell_btn_object.configure(text = self.number_of_surrounding_mines)
        self.is_opened = True

        self.cell_btn_object.configure(
            bg='SystemButtonFace'
        )

    def pressed_mine(self) :
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit()



    def get_cell(self,x, y):
        for cell in Cell.all:
            if cell.x ==x and cell.y ==y:
                return cell


    @property
    def surrounding_mines(self):
        cells=[
            self.get_cell(self.x-1, self.y-1 ),
            self.get_cell(self.x - 1, self.y ),
            self.get_cell(self.x - 1, self.y+1),
            self.get_cell(self.x , self.y-1),
            self.get_cell(self.x , self.y+1),
            self.get_cell(self.x + 1, self.y - 1),
            self.get_cell(self.x + 1, self.y),
            self.get_cell(self.x + 1, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells


    @property
    def number_of_surrounding_mines(self):
        counter = 0
        for cell in self.surrounding_mines:
            if cell.is_mine == True:
                counter = counter + 1

        return counter






    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

    def randomized_mines():
        mine_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for mine_cell in mine_cells:
            mine_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"


