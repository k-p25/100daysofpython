from tkinter import *

window = Tk()
window.title("Mile to KM converter")
# window.minsize(width=400, height=200)
window.config(padx=30, pady=30)

for i in range (2):
    window.columnconfigure(i, pad = 10)
    window.rowconfigure(i, pad = 10)

def convert():
    if input.get():
        converted["text"] = int(input.get()) * 1.609

input = Entry(width=10, )
input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

ieq = Label(text="is equal to")
ieq.grid(column=0, row=1)

converted = Label(text="0")
converted.grid(column=1, row=1)

km = Label(text="KM")
km.grid(column=2, row=1)

calculate = Button(text="calculate", command=convert)
calculate.grid(column=1, row=2)








window.mainloop()