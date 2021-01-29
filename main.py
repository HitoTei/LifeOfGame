import threading
import tkinter as tk

Height = 20
Width = 20

baseGround = tk.Tk()
baseGround.geometry('800x800')
baseGround.title('ライフゲーム')

boolArray = []


def is_checked(x, y):
    global boolArray
    if not is_within_range(x, y):
        return False
    return boolArray[x][y].get()


def count_around_check(x, y):
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    count = 0
    for i in range(0, 8):
        if is_checked(x + dx[i], y + dy[i]):
            count += 1
    return count


def next_check_box_state(x, y):
    global boolArray
    count = count_around_check(x, y)
    if boolArray[x][y].get():
        return count == 2 or count == 3
    else:
        return count == 3


def is_within_range(x, y):
    global Height, Width
    is_x_in = 0 <= x < Height
    is_y_in = 0 <= y < Width
    return is_x_in and is_y_in


def go_next_state():
    global boolArray, Height, Width
    next_state = []

    for x in range(0, Height):
        array = []
        for y in range(0, Width):
            next_val: bool = next_check_box_state(x, y)
            array.append(next_val)
        next_state.append(array)
    for x in range(0, Height):
        for y in range(0, Width):
            boolArray[x][y].set(next_state[x][y])


for i in range(0, Height):
    a = []
    for j in range(0, Width):
        a.append(tk.BooleanVar(value=False))
    boolArray.append(a)
for i in range(0, Height):
    for j in range(0, Width):
        tk.Checkbutton(variable=boolArray[i][j]).grid(row=i, column=j)

tk.Button(command=go_next_state, text="次の状態に進める").grid(row=Height + 1, column=Width + 1)

baseGround.mainloop()
