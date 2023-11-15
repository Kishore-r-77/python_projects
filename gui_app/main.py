import tkinter

window = tkinter.Tk()

window.title("My First Gui App")
window.minsize(width=500, height=300)


def button_clicked():
    print("I got Clicked")
    my_label.config(text=my_input.get())


# Label
my_label = tkinter.Label(text="I'm a Label", font=("Ariel", 24, "bold"))
# my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="Kishore")
# my_label.place(x=0,y=0)
my_label.grid(column=1, row=0)

# Button
my_button = tkinter.Button(text="Click me", command=button_clicked)
# my_button.pack()
my_button.grid(column=1, row=2)

# Entry
my_input = tkinter.Entry(width=10)
# my_input.pack()
my_input.grid(column=1, row=3)

window.mainloop()
