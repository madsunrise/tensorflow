# -*- coding: utf-8 -*-
from Tkinter import *
from matrix import Matrix

MATRIX_SIZE = 28
COEFFICIENT = 15
CANVAS_SIDE = (MATRIX_SIZE - 1) * COEFFICIENT


class CanvasApp(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=None)
        self.x = self.y = 0
        self.canvas = Canvas(self, cursor="cross", width=CANVAS_SIDE, height=CANVAS_SIDE)

        self.sbarv = Scrollbar(self, orient=VERTICAL)
        self.sbarh = Scrollbar(self, orient=HORIZONTAL)
        self.sbarv.config(command=self.canvas.yview)
        self.sbarh.config(command=self.canvas.xview)

        self.canvas.config(yscrollcommand=self.sbarv.set)
        self.canvas.config(xscrollcommand=self.sbarh.set)

        self.canvas.grid(row=0, column=0, sticky=N + S + E + W)
        self.sbarv.grid(row=0, column=1, stick=N + S)
        self.sbarh.grid(row=1, column=0, sticky=E + W)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.prev_x = None
        self.prev_y = None

        self.matrix = Matrix(MATRIX_SIZE, MATRIX_SIZE)

    def on_button_press(self, event):
        self.prev_x = self.canvas.canvasx(event.x)
        self.prev_y = self.canvas.canvasy(event.y)

    def on_move_press(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        if cur_x < 0:
            cur_x = 0
        if cur_y < 0:
            cur_y = 0
        if cur_x > CANVAS_SIDE:
            cur_x = CANVAS_SIDE
        if cur_y > CANVAS_SIDE:
            cur_y = CANVAS_SIDE

        self.canvas.create_line(self.prev_x, self.prev_y, cur_x, cur_y)
        self.prev_x = cur_x
        self.prev_y = cur_y  # Запоминаем текущую точку
        print (int(cur_x), int(cur_y))
        self.matrix.set_value(int(cur_y) / COEFFICIENT, int(cur_x) / COEFFICIENT, 1)

    def on_button_release(self, event):
        self.matrix.print_matrix()


if __name__ == "__main__":
    root = Tk()
    root.resizable(width=False, height=False)
    app = CanvasApp(root)
    app.pack()
    root.mainloop()
