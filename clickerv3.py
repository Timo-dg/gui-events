import tkinter as tk

gui = tk.Tk()
gui.title('Clicker v1')
gui.geometry('250x200')
gui.config(bg="grey")
clicks = 0
check = ''

def colors():
    if clicks < 0:
        gui.config(bg='red')
    elif clicks > 0:
        gui.config(bg='green')
    else:
        gui.config(bg='grey')

def up():
    global clicks,check
    clicks += 1
    counter.config(text=clicks)
    counter.pack()
    check='up'
    gui.after(10,colors)

def down():
    global clicks,check
    clicks -= 1
    counter.config(text=clicks)
    counter.pack()
    check='down'
    gui.after(10,colors)

def on_enter(e):
   gui.config(bg='yellow')
def on_leave(e):
   gui.config(bg='grey')
    
def doubleclick(e):
    global check, clicks
    if check == 'up':
        clicks *= 3
    elif check == 'down':
        clicks /=3
    counter.config(text= clicks)

button_up = tk.Button(gui,text='up', font=('arial',20,'bold'),command=up)
button_up.grid()
button_up.config(
    padx=30
)
button_up.pack()
pady=30

counter = tk.Label(
    gui,
    text=clicks
)
counter.pack()

button_down = tk.Button(gui,text='down', font=('arial',20,'bold'),command=down)
button_down.config(
    padx=30
)
button_down.pack()
pady=30

button_up.bind("<Enter>", on_enter)
button_up.bind("<Leave>", on_leave)
button_down.bind("<Enter>", on_enter)
button_down.bind("<Leave>", on_leave)
counter.bind('<Double-Button>', doubleclick)

gui.mainloop()