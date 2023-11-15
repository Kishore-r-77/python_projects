import tkinter

window = tkinter.Tk()

window.title("My First Gui App")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I'm a Label")
my_label.pack()

window.mainloop()
