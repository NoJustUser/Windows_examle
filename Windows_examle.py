from tkinter import *

def draw_shape(x1, y1, x2, y2, var):
    if var.get() == 1:
        canvas.create_rectangle(x1, y1, x2, y2)
    elif var.get() == 0:
        canvas.create_oval(x1, y1, x2, y2)


def create_shape():

    def close_win():
        win_for_create.grab_release()
        win_for_create.destroy()


    r_var = IntVar()
    r_var.set(0)

    win_for_create = Toplevel()
    win_for_create.title('shape')
    win_for_create.geometry('287x280')
    win_for_create.grab_set()          # захватываем пользовательский ввод

    frame_x1y1 = Frame(win_for_create)
    frame_x2y2 = Frame(win_for_create)
    frame_rbutton_ov = Frame(win_for_create)
    frame_rbutton_rec = Frame(win_for_create)

    label_x1 = Label(frame_x1y1, text="X1", padx=5)
    label_y1 = Label(frame_x1y1, text="Y1", padx=25)
    label_x2 = Label(frame_x2y2, text="X2", padx=5)
    label_y2 = Label(frame_x2y2, text="Y2", padx=25)
    entry_x1 = Entry(frame_x1y1, width=7)
    entry_y1 = Entry(frame_x1y1, width=7)
    entry_x2 = Entry(frame_x2y2, width=7)
    entry_y2 = Entry(frame_x2y2, width=7)

    button_oval = Radiobutton(frame_rbutton_ov, text='Круг', variable=r_var, value=0, padx=50)
    button_rect = Radiobutton(frame_rbutton_rec, text='Прямоугольник', variable=r_var, value=1, padx=50)

    btn_draw = Button(win_for_create, text='Нарисовать', width=30, height=2, 
                      command=lambda: [draw_shape(entry_x1.get(), entry_y1.get(), entry_x2.get(), entry_y2.get(), r_var), 
                      close_win()],
                      bg='#c2c2c2')

    w1 = w + 310
    h1 = h + 35
    win_for_create.geometry('+{}+{}'.format(w1, h1))
    frame_x1y1.pack()
    frame_x2y2.pack()
    frame_rbutton_ov.pack(anchor=W)
    frame_rbutton_rec.pack(anchor=W)
    label_x1.pack(side=LEFT)
    entry_x1.pack(side=LEFT)
    label_y1.pack(side=LEFT)
    entry_y1.pack(side=LEFT)
    label_x2.pack(side=LEFT)
    entry_x2.pack(side=LEFT)
    label_y2.pack(side=LEFT)
    entry_y2.pack(side=LEFT)
    button_oval.pack()
    button_rect.pack()
    btn_draw.pack(pady=60)


 

root = Tk()
root.config(bg='#C0C0C0')

frame_left = Frame(root, width=300, height=445, bg='#C0C0C0')
frame_right = Frame(root, width=300, height=445, bg='#C0C0C0')

canvas = Canvas(frame_left, width=300, height=390, bg='white')
button_create = Button(frame_left, text='Добавить фигуру', height=2, command=create_shape)

frame_left.pack(side=LEFT)
frame_right.pack(side=RIGHT)
canvas.pack()
button_create.pack(fill=X)

root.update_idletasks()              # перезагружаем данные об окне

s = root.geometry()                  # Получаем размер окна
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])

root.title("Rectange or Oval")

w = root.winfo_screenwidth() // 2    # Середина экрана
h = root.winfo_screenheight() // 2

w = w - width_root//2
h = h - height_root//2

root.geometry('+{}+{}'.format(w, h)) # Устанавливаем окно в центр экрана
root.resizable(False, False)
 
root.mainloop()
