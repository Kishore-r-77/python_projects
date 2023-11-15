import tkinter

window = tkinter.Tk()

window.title("My First Gui App")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I'm a Label", font=("Ariel", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"

my_label.config(text="Kishore")


def button_clicked():
    print("I got Clicked")
    my_label.config(text=my_input.get())


# Button
my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.pack()

# Entry
my_input = tkinter.Entry(width=10)
my_input.pack()

window.mainloop()
