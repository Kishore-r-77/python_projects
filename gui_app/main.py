import tkinter

window = tkinter.Tk()

window.title("My First Gui App")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I'm a Label", font=("Ariel", 24, "bold"))
my_label.pack()

window.mainloop()
